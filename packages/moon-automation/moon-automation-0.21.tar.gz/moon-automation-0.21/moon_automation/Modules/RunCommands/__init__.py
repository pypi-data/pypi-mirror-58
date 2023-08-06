from jinja2 import Template

from moon_automation.BaseModule import BaseModule


class RunCommands(BaseModule):

    def __init__(self,devices,extra={},config="config.yaml",**kwargs):
        super().__init__(devices,extra,config,**kwargs)

    async def run(self):
        for device,info in self.config["devices"].items():
            await self.run_commands_by_template(self.devices[device],info)


    async def run_commands_by_template(self,device,info):
        template = Template(info["commands"])
        commands = template.render(info)
        results = await device.async_run_commands(commands)
        if self.config.get("log_output"):
            with open("{}/{}".format(self.config["output_folder"],self.config["output_name"].format(device)),"w+") as file:
                for result in results:
                    file.write(result)
                    file.write("-" * 20)
        for result in results:
            print(result)
            print("-"*20)
        return {"command_output":results}



