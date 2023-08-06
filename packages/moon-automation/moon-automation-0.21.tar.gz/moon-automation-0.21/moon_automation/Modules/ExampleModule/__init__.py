from moon_automation.BaseModule import BaseModule


class ExampleModule(BaseModule):

    def __init__(self,devices,extra={},config="config.yaml",**kwargs):
        super().__init__(devices,extra,config,**kwargs)

    async def run(self):
        print("SMILE :)")
        return {"DATA":"A LOOOOOT OF DATA"}