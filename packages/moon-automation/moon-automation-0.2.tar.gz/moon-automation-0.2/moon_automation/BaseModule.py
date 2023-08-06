import inspect

import yaml


class BaseModule(object):

    def __init__(self,devices,extra_args={},config=None,**kwargs):
        self.devices=devices
        self.extra_args=extra_args
        self.load_config(config)

    @staticmethod
    def _default_config():
        config={
        }
        return config

    @classmethod
    def _generate_config(cls):
        return yaml.dump(cls._default_config(), default_flow_style=False)

    def run(self):
        raise Exception("Module {} has not defined run function yet".format(str(self)))
        pass

    def load_config(self,config_file):
        """
        load config.yaml
        :return:
        """
        if not config_file:
            curdir = inspect.getfile(self.__class__)[0:-11]
            config_path=curdir+"config.yaml"
        else:
            config_path=config_file
        with open(config_path) as f:
            self.config = yaml.load(f.read())
