import asyncio

from moon_automation.DeviceTypes.CiscoIOSXR import CiscoIOSXR
from moon_automation.DeviceTypes.CiscoNexus import CiscoNexus

if __name__ == '__main__':

    c = CiscoIOSXR("R1","10.75.58.78","23","cisco","cisco",protocol="telnet",debug=True)

    n = CiscoNexus("R2","10.75.37.150","22","admin","cisco","ssh",debug=True)


    # loop = asyncio.get_event_loop()

    # loop.run_until_complete(c._telnet_async())
    
    # resp = n.run_commands(["show run","show int brief"])
    # for i in resp:
    #     print(i)
    # # pprint(n.run_commands(["show run","show int brief"]))
    # 
    # resp = n.run_commands(["show run"])
    # for i in resp:
    #     print(i)
    # c.run_commands("show run")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(c.async_configure("no username ljm625"))

    # resp =await c.run_commands("show run")
    # print(resp)
    # resp = c.configure("no username ljm625")
    # n.configure("no username ljm625")

    # c._telnet()