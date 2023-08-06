# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,protected-access,line-too-long,broad-except,bare-except,invalid-name
import os
import sys
import logging
import threading
import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from . import const
from .proxy import LockingServerProxy
from . import device_logic

LOG = logging.getLogger(__name__)
if sys.stdout.isatty():
    logging.basicConfig(level=logging.DEBUG)

def initParamsets():
    with open(const.PARAMSETS_DB, 'w') as fptr:
        fptr.write("{}")

# pylint: disable=too-many-instance-attributes
class RPCFunctions():
    """
    Object holding the methods the XML-RPC server should provide.
    """
    def __init__(self, devices, persistance, logic):
        LOG.debug("RPCFunctions.__init__")
        self.remotes = {}
        try:
            self.active = False
            self.knownDevices = []
            self.interface_id = "pydevccu"
            self.persistance = persistance
            self.devices = []
            self.paramset_descriptions = {}
            self.supported_devices = {}
            self.paramsets = {}
            self.paramset_callbacks = []
            self.active_devices = []
            self.logic = logic
            self.logic_devices = []
            self._loadDevices(devices)
            if not os.path.exists(const.PARAMSETS_DB) and persistance:
                initParamsets()
            self._loadParamsets()
        except Exception as err:
            LOG.debug("RPCFunctions.__init__: Exception: %s", err)
            self.devices = []

    # pylint: disable=too-many-locals
    def _loadDevices(self, devices=None):
        added_devices = []
        if devices is not None:
            LOG.info("RPCFunctions._loadDevices: Limiting to devices: %s", devices)
        script_dir = os.path.dirname(__file__)
        dd_path = os.path.join(script_dir, const.DEVICE_DESCRIPTIONS)
        pd_path = os.path.join(script_dir, const.PARAMSET_DESCRIPTIONS)
        for filename in os.listdir(dd_path):
            devname = filename.split('.')[0].replace('_', ' ')
            if devname in self.active_devices:
                continue
            if devices is not None:
                if devname not in devices:
                    continue
            with open(os.path.join(dd_path, filename)) as fptr:
                dd = json.load(fptr)
                self.devices.extend(dd)
                added_devices.extend(dd)
                for device in dd:
                    d_addr = device.get(const.ATTR_ADDRESS)
                    if not ':' in d_addr:
                        self.supported_devices[devname] = d_addr
                        break
            with open(os.path.join(pd_path, filename)) as fptr:
                pd = json.load(fptr)
                for k, v in pd.items():
                    self.paramset_descriptions[k] = v
            if self.logic and devname in device_logic.DEVICE_MAP.keys():
                logic_module = device_logic.DEVICE_MAP.get(devname)
                logic_device = logic_module(self, **self.logic)
                logic_device.active = True
                self.logic_devices.append(logic_device)
                logic_thread = threading.Thread(name=logic_device.name,
                                                target=logic_device.work,
                                                daemon=True)
                logic_thread.start()
            self.active_devices.append(devname)
        return added_devices

    # pylint: disable=too-many-branches
    def _removeDevices(self, devices=None):
        remove_devices = devices
        if remove_devices is None:
            remove_devices = self.active_devices[:]
        addresses = []
        for devname in remove_devices:
            if devname in self.active_devices:
                self.active_devices.remove(devname)
            if devname in self.supported_devices:
                del self.supported_devices[devname]
            for dd in self.devices:
                del_address = None
                address = dd.get(const.ATTR_ADDRESS)
                try:
                    if not ':' in address and dd.get(const.ATTR_TYPE) == devname:
                        del_address = address
                    elif ':' in address and dd.get(const.ATTR_PARENT_TYPE) == devname:
                        del_address = address
                    if del_address is None:
                        continue
                    addresses.append(del_address)
                    if del_address in self.paramset_descriptions:
                        del self.paramset_descriptions[del_address]
                    if del_address in self.paramsets:
                        del self.paramsets[del_address]
                except Exception as err:
                    LOG.warning("_removeDevices: Failed to remove %s: %s", devname, err)
            for logic_device in self.logic_devices:
                if logic_device.name == devname:
                    logic_device.active = False
                    self.logic_devices.remove(logic_device)
        self.devices = [d for d in self.devices if d.get(const.ATTR_ADDRESS) not in addresses]
        for interface_id, proxy in self.remotes.items():
            proxy.deleteDevices(interface_id, addresses)

    def _loadParamsets(self):
        if self.persistance:
            with open(const.PARAMSETS_DB) as fptr:
                self.paramsets = json.load(fptr)

    def _saveParamsets(self):
        LOG.debug("Saving paramsets")
        if self.persistance:
            with open(const.PARAMSETS_DB, 'w') as fptr:
                json.dump(self.paramsets, fptr)

    def _askDevices(self, interface_id):
        self.knownDevices = self.remotes[interface_id].listDevices(interface_id)
        LOG.debug("RPCFunctions._askDevices: %s", self.knownDevices)
        t = threading.Thread(name='_pushDevices',
                             target=self._pushDevices,
                             args=(interface_id, ))
        t.start()

    def _pushDevices(self, interface_id):
        newDevices = []
        deleteDevices = []
        knownDeviceAddresses = []
        for device in self.knownDevices:
            if device[const.ATTR_ADDRESS] not in self.paramset_descriptions.keys():
                deleteDevices.append(device[const.ATTR_ADDRESS])
            else:
                knownDeviceAddresses.append(device[const.ATTR_ADDRESS])
        for device in self.devices:
            if device[const.ATTR_ADDRESS] not in knownDeviceAddresses:
                newDevices.append(device)
        if newDevices:
            self.remotes[interface_id].newDevices(interface_id, newDevices)
        if deleteDevices:
            self.remotes[interface_id].deleteDevices(interface_id, deleteDevices)
        LOG.debug("RPCFunctions._pushDevices: pushed")

    def _fireEvent(self, interface_id, address, value_key, value):
        address = address.upper()
        LOG.debug("RPCFunctions._fireEvent: %s, %s, %s, %s", interface_id, address, value_key, value)
        for callback in self.paramset_callbacks:
            callback(interface_id, address, value_key, value)
        for pinterface_id, proxy in self.remotes.items():
            proxy.event(pinterface_id, address, value_key, value)

    def listDevices(self, interface_id=None):
        LOG.debug("RPCFunctions.listDevices: interface_id = %s", interface_id)
        return self.devices

    # pylint: disable=no-self-use
    def getServiceMessages(self):
        LOG.debug("RPCFunctions.getServiceMessages")
        return [['VCU0000001:1', const.ATTR_ERROR, 7]]

    def getValue(self, address, value_key):
        address = address.upper()
        LOG.debug("RPCFunctions.getValue: address=%s, value_key=%s", address, value_key)
        return self.getParamset(address, const.PARAMSET_ATTR_VALUES)[value_key]

    def setValue(self, address, value_key, value, force=False):
        address = address.upper()
        LOG.debug("RPCFunctions.setValue: address=%s, value_key=%s, value=%s, force=%s", address, value_key, value, force)
        paramset = {value_key: value}
        self.putParamset(address, const.PARAMSET_ATTR_VALUES, paramset, force=force)
        return ""

    # pylint: disable=too-many-arguments
    def putParamset(self, address, paramset_key, paramset, force=False):
        address = address.upper()
        LOG.debug("RPCFunctions.putParamset: address=%s, paramset_key=%s, paramset=%s, force=%s", address, paramset_key, paramset, force)
        paramsets = self.paramset_descriptions[address]
        paramset_values = paramsets[paramset_key]
        for value_key, value in paramset.items():
            param_data = paramset_values[value_key]
            param_type = param_data[const.ATTR_TYPE]
            if not const.PARAMSET_OPERATIONS_WRITE & param_data[const.PARAMSET_ATTR_OPERATIONS] and not force:
                LOG.warning(
                    "RPCFunctions.putParamset: address=%s, value_key=%s: write operation not allowed", address, value_key)
                raise Exception
            if param_type == const.PARAMSET_TYPE_ACTION:
                self._fireEvent(self.interface_id, address, value_key, True)
                return
            if param_type == const.PARAMSET_TYPE_BOOL:
                value = bool(value)
            if param_type == const.PARAMSET_TYPE_STRING:
                value = str(value)
            if param_type in [const.PARAMSET_TYPE_INTEGER, const.PARAMSET_TYPE_ENUM]:
                value = int(float(value))
            if param_type == const.PARAMSET_TYPE_FLOAT:
                value = float(value)
            if param_type == const.PARAMSET_TYPE_ENUM:
                if value > float(param_data[const.PARAMSET_ATTR_MAX]):
                    LOG.warning("RPCFunctions.putParamset: address=%s, value_key=%s: value too high", address, value_key)
                    raise Exception
                if value < float(param_data[const.PARAMSET_ATTR_MIN]):
                    LOG.warning("RPCFunctions.putParamset: address=%s, value_key=%s: value too low", address, value_key)
                    raise Exception
            if param_type in [const.PARAMSET_TYPE_FLOAT, const.PARAMSET_TYPE_INTEGER]:
                special = param_data.get(const.PARAMSET_ATTR_SPECIAL, [])
                valid = []
                for special_value in special:
                    for _, v in special_value:
                        valid.append(v)
                value = float(value)
                if param_type == const.PARAMSET_TYPE_INTEGER:
                    value = int(value)
                if value not in valid:
                    max_val = float(param_data[const.PARAMSET_ATTR_MAX])
                    min_val = float(param_data[const.PARAMSET_ATTR_MIN])
                    if param_type == const.PARAMSET_TYPE_INTEGER:
                        max_val = int(max_val)
                        min_val = int(min_val)
                    if value > max_val:
                        value = max_val
                    if value < min_val:
                        value = min_val
            if address not in self.paramsets:
                self.paramsets[address] = {}
            if paramset_key not in self.paramsets[address]:
                self.paramsets[address][paramset_key] = {}
            self.paramsets[address][paramset_key][value_key] = value
            self._fireEvent(self.interface_id, address, value_key, value)

    def getDeviceDescription(self, address):
        address = address.upper()
        LOG.debug("RPCFunctions.getDeviceDescription: address=%s", address)
        for device in self.devices:
            if device.get(const.ATTR_ADDRESS) == address:
                return device
        raise Exception

    def getParamsetDescription(self, address, paramset_type):
        address = address.upper()
        LOG.debug("RPCFunctions.getParamsetDescription: address=%s, paramset_type=%s", address, paramset_type)
        return self.paramset_descriptions[address][paramset_type]

    def getParamset(self, address, paramset_key, mode=None):
        address = address.upper()
        LOG.debug("RPCFunctions.getParamset: address=%s, paramset_key=%s", address, paramset_key)
        if mode is not None:
            LOG.debug("RPCFunctions.getParamset: mode argument not supported")
            raise Exception
        if paramset_key not in [const.PARAMSET_ATTR_MASTER, const.PARAMSET_ATTR_VALUES]:
            raise Exception
        data = {}
        pd = self.paramset_descriptions[address][paramset_key]
        for parameter in pd.keys():
            if pd[parameter][const.ATTR_FLAGS] & const.PARAMSET_FLAG_INTERNAL:
                continue
            try:
                data[parameter] = self.paramsets[address][paramset_key][parameter]
            except:
                data[parameter] = self.paramset_descriptions[address][paramset_key][parameter][const.PARAMSET_ATTR_DEFAULT]
        return data

    def init(self, url, interface_id=None):
        LOG.debug("RPCFunctions.init: url=%s, interface_id=%s", url, interface_id)
        if interface_id is not None:
            try:
                self.remotes[interface_id] = LockingServerProxy(url)
                t = threading.Thread(name='_askDevices',
                                     target=self._askDevices,
                                     args=(interface_id, ))
                t.start()
            except Exception as err:
                LOG.debug("RPCFunctions.init:Exception: %s", err)
        else:
            deletedremote = None
            for remote in self.remotes:
                if self.remotes[remote]._ServerProxy__host in url:
                    deletedremote = remote
                    break
            if deletedremote is not None:
                del self.remotes[deletedremote]
        return ""

class RequestHandler(SimpleXMLRPCRequestHandler):
    """We handle requests to / and /RPC2"""
    rpc_paths = ('/', '/RPC2',)

class ServerThread(threading.Thread):
    """XML-RPC server thread to handle messages from CCU / Homegear"""
    def __init__(self, addr=(const.IP_LOCALHOST_V4, const.PORT_RF),
                 devices=None, persistance=False, logic=False):
        LOG.debug("ServerThread.__init__")
        threading.Thread.__init__(self)
        self.addr = addr
        LOG.debug("__init__: Registering RPC methods")
        self._rpcfunctions = RPCFunctions(devices, persistance, logic)
        LOG.debug("ServerThread.__init__: Setting up server")
        self.server = SimpleXMLRPCServer(addr, requestHandler=RequestHandler,
                                         logRequests=False, allow_none=True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        LOG.debug("ServerThread.__init__: Registering RPC functions")
        self.server.register_instance(
            self._rpcfunctions, allow_dotted_names=True)

    def run(self):
        LOG.info("Starting server at http://%s:%i", self.addr[0], self.addr[1])
        self._rpcfunctions.active = True
        self.server.serve_forever()

    def stop(self):
        """Shut down our XML-RPC server."""
        self._rpcfunctions.active = False
        for logic_device in self._rpcfunctions.logic_devices:
            logic_device.active = False
        self._rpcfunctions._saveParamsets()
        LOG.info("Shutting down server")
        self.server.shutdown()
        LOG.debug("ServerThread.stop: Stopping ServerThread")
        self.server.server_close()
        LOG.info("Server stopped")

    # Convenience methods at server scope
    def setValue(self, address, value_key, value, force=False):
        return self._rpcfunctions.setValue(address, value_key, value, force)

    def getValue(self, address, value_key):
        return self._rpcfunctions.getValue(address, value_key)

    def getDeviceDescription(self, address):
        return self._rpcfunctions.getDeviceDescription(address)

    def getParamsetDescription(self, address, paramset):
        return self._rpcfunctions.getParamsetDescription(address, paramset)

    def getParamset(self, address, paramset):
        return self._rpcfunctions.getParamset(address, paramset)

    def putParamset(self, address, paramset_key, paramset, force=False):
        return self._rpcfunctions.putParamset(address, paramset_key, paramset, force)

    def listDevices(self):
        return self._rpcfunctions.listDevices()

    def getServiceMessages(self):
        return self._rpcfunctions.getServiceMessages()

    def supportedDevices(self):
        return self._rpcfunctions.supported_devices

    def addDevices(self, devices=None):
        devices = self._rpcfunctions._loadDevices(devices=devices)
        for interface_id, proxy in self._rpcfunctions.remotes.items():
            LOG.debug("addDevices: Pushing new devices to %s", interface_id)
            proxy.newDevices(interface_id, devices)

    def removeDevices(self, devices=None):
        self._rpcfunctions._removeDevices(devices)
