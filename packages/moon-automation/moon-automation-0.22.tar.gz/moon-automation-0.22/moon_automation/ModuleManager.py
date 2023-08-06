import importlib


class ModuleManager(object):

    def __init__(self,module_name,devices_list,input,debug=False,**kwargs):
        self.module_name = module_name
        self.devices=devices_list
        self.input=input
        self.debug=debug
        self.load(**kwargs)

    @staticmethod
    def _get_class(module_name, class_name):
        try:
            # Try if module exists in current workdir (for override)
            # Otherwise load from automation lib
            m = importlib.import_module("{}.{}".format(module_name, class_name))
            # get the class, will raise AttributeError if class cannot be found
            return getattr(m, class_name)
        except:
            pass
        try:
            # load the module, will raise ImportError if module cannot be loaded
            m = importlib.import_module("moon_automation.{}.{}".format(module_name, class_name))
            # get the class, will raise AttributeError if class cannot be found
            return getattr(m, class_name)
        except Exception as e:
            raise Exception("Module {} not valid".format(module_name))

    def load(self,**kwargs):
        # if self.debug:
        #     cls = self._get_class(module_name="ModulesRepo",class_name=self.module_name)
        # else:
        cls = self._get_class(module_name="Modules",class_name=self.module_name)

        self.obj = cls(self.devices,input,**kwargs)

    async def dispatch(self):
        resp = await self.obj.run()
        return resp