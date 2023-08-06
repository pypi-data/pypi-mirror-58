import yaml

from moon_automation.DeviceParser import DeviceParser
from moon_automation.ModuleManager import ModuleManager


def load(fp):
    with open(fp) as f:
        config = yaml.load(f.read())
        return config


if __name__ == '__main__':


    config = load("config.yaml")

    parser = DeviceParser(test_bed_yaml=config["topology"])
    devices = parser.generate_devices()

    # Load modules
    modules = config["modules"]

    # Dispatch modules
    resp = {}
    for module in modules:
        print("Running Module {}".format(module))
        if type(module)==str:
            resp = ModuleManager(module_name=module,devices_list=devices,input=resp,debug=config.get("debug")).dispatch()
        elif type(module)==dict:
            module_name = [*module][0]
            resp = ModuleManager(module_name=module_name,devices_list=devices,input=resp,debug=config.get("debug"),**module[module_name]).dispatch()


    #
    # print(devices["R1"].run_commands(["show run"])[0])
    # print(devices["R2"].run_commands(["show run"])[0])
