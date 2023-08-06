from moon_automation.DeviceTypes.BaseDevice import BaseDevice


class CiscoNexus(BaseDevice):

    def __init__(self,name,hostname,port,username,password,protocol,debug=False):
        super().__init__(name=name,hostname=hostname,port=port,username=username,password=password,protocol=protocol,enable=None,debug=debug)
        self.handler = None


    def _terminal_length_zero(self):
        self.handler.sendline("terminal length 0")
        pass

    def _run_commands(self,commands):
        resp=[]
        for command in commands:
            self.handler.send("{}\n##\n".format(command))
            self.expect(r"[>|#|$]\s? ##")
            resp.append(str(self.handler.before,encoding="utf-8"))
            # print("---------------------------")
        return resp

    async def _async_run_commands(self,commands):
        resp=[]
        for command in commands:
            self.handler.send("{}\n##\n".format(command))
            await self.async_expect(r"[>|#|$]\s? ##")
            resp.append(str(self.handler.before,encoding="utf-8"))
            # print("---------------------------")
        return resp

    def _configure(self,func,commands):
        self.handler.send("{}\n##\n".format("config t"))
        self.expect(r"config\)[>|#|$]\s? ##")
        resp = func(commands)
        self.handler.send("end\n##\n")
        self.expect(r"[>|#|$]\s? ##")
        return resp

    async def _async_configure(self,func,commands):
        self.handler.send("{}\n##\n".format("config t"))
        await self.async_expect(r"config\)[>|#|$]\s? ##")
        resp =await func(commands)
        self.handler.send("end\n##\n")
        await self.async_expect(r"[>|#|$]\s? ##")
        return resp
