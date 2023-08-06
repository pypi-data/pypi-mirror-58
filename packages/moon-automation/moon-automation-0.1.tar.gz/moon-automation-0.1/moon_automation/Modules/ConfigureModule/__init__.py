from jinja2 import Template

from moon_automation.BaseModule import BaseModule


class ConfigureModule(BaseModule):

    def __init__(self,devices,extra={},config="config.yaml",**kwargs):
        super().__init__(devices,extra,config,**kwargs)

    async def run(self):
        for device,info in self.config["devices"].items():
            await self.configure_by_template(self.devices[device],info)


    async def configure_by_template(self,device,info):
        template = Template(info["template"])
        config = template.render(info)
        await device.async_configure(config)



