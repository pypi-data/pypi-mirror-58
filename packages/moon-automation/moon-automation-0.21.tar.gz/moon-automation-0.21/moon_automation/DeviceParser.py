import yaml

from moon_automation.DeviceTypes.CiscoIOSXR import CiscoIOSXR
from moon_automation.DeviceTypes.CiscoNexus import CiscoNexus


class DeviceParser(object):
    """
    Example testbed.yaml:

    ---
    devices:
      R1:
            connections:
              cli:
                    ip: 10.75.1.1
                    port: 22
                    protocol: ssh
            credentials:
              default:
                    password: cisco
                    username: cisco
            os: iosxr
            type: iosxr
      R2:
            connections:
              cli:
                    ip: 10.75.1.2
                    port: 23
                    protocol: telnet
            credentials:
              default:
                    password: cisco
                    username: admin
              enable:
                    password: cisco
            os: nxos
            type: nxos
    """

    def __init__(self,test_bed_yaml):
        self.test_bed_file=test_bed_yaml
        pass

    def load(self):
        with open(self.test_bed_file) as f:
            config = yaml.load(f.read())
            return config

    def generate_devices(self):
        config = self.load()
        devices = {}
        for device_name,device_info in config.get("devices").items():
            connect_info = device_info.get("connections").get("cli")
            credentials = device_info.get("credentials")
            if credentials.get("default"):
                username = credentials.get("default").get("username")
                password = credentials.get("default").get("password")
            elif len(credentials)>=1:
                for k,v in credentials.items():
                    username = v.get("username")
                    password = v.get("password")
                    break
            else:
                raise Exception("ERROR : Device {}'s credentials not given".format(device_name))
            if device_info.get("enable"):
                enable = device_info.get("enable").get("password")
            if device_info.get("os")=="iosxr":
                device = CiscoIOSXR(name=device_name,hostname=connect_info["ip"],port=connect_info["port"],
                                    username=username,password=password,protocol=connect_info["protocol"])
            elif device_info.get("os")=="nxos":
                device = CiscoNexus(name=device_name,hostname=connect_info["ip"],port=connect_info["port"],
                                    username=username,password=password,protocol=connect_info["protocol"])
            else:
                raise Exception("Device os {} not supported".format(device_info.get("os")))
            devices[device_name]=device
        return devices

