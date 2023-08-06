from moon_automation.BaseModule import BaseModule


class BackupConfig(BaseModule):

    def __init__(self,devices,extra={},config="config.yaml",**kwargs):
        super().__init__(devices,extra,config,**kwargs)

    async def run(self):
        for device,info in self.devices.items():
            resp = await self.devices[device].async_run_commands("show run")
            with open("{}/{}".format(self.config["output_folder"],self.config["output_name"].format(device)),"w+") as file:
                file.write(resp[0])


