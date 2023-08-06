from moon_automation.DeviceTypes.BaseDevice import BaseDevice


class CiscoIOSXR(BaseDevice):

    def __init__(self,name,hostname,port,username,password,protocol,debug=False):
        super().__init__(name=name,hostname=hostname,port=port,username=username,password=password,protocol=protocol,enable=None,debug=debug)
        self.handler = None


    def _terminal_length_zero(self):
        self.sendline("terminal length 0")

    def _run_commands(self,commands):
        resp=[]
        for command in commands:
            self.handler.send("{}\n##\n".format(command))
            self.expect(r"[>|#|$]\s?##")
            resp.append(str(self.handler.before,encoding="utf-8"))
            self.expect("marker.")
            # print(self.handler.after)
        return resp

    async def _async_run_commands(self,commands):
        resp=[]
        for command in commands:
            self.handler.send("{}\n##\n".format(command))
            await self.async_expect(r"[>#\$]\s?##")
            resp.append(str(self.handler.before,encoding="utf-8"))
            await self.async_expect("marker.")
            # print(self.handler.after)
        return resp


    def _configure(self,func,commands):
        self.handler.send("{}\n##\n".format("config t"))
        self.expect(r"config\)[>#\$]\s?##")
        resp = func(commands)
        self.handler.send("commit\nabort\n##\n")
        self.expect(r"[>|#|$]\s?##")
        self.expect("marker.")
        return resp

    async def _async_configure(self,func,commands):
        self.handler.send("{}\n##\n".format("config t"))
        await self.async_expect(r"config\)[>|#|$]\s?##")
        resp =await func(commands)
        self.handler.send("commit\nabort\n##\n")
        await self.async_expect(r"[>#\$]\s?##")
        await self.async_expect("marker.")
        return resp

