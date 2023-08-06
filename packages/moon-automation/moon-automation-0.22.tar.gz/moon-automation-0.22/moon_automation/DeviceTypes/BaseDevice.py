import re

import pexpect


class BaseDevice(object):

    def __init__(self,name,hostname,port,username,password,protocol,enable,debug):
        self.name=name
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.protocol=protocol
        self.debug=debug
        pass

    def expect(self,param,timeout=None):
        a = self.handler.expect(param,timeout=timeout)
        if self.debug:
            print(self.handler.before.decode('utf-8'))
            print(a)
            print(self.handler.after.decode('utf-8'))
            print("---------------------------")

        return a

    async def async_expect(self,param,timeout=None):
        a = await self.handler.expect(param,timeout=timeout,async_=True)
        if self.debug:
            print(self.handler.before.decode('utf-8'))
            print(a)
            print(self.handler.after.decode('utf-8'))
            print("---------------------------")
        return a



    def sendline(self,param):
        return self.handler.sendline(param)

    async def _async_connect(self):
        if self.protocol == "ssh":
            await self._ssh_async()
        else:
            await self._telnet_async()


    def _connect(self):
        if self.protocol == "ssh":
            self._ssh()
        else:
            self._telnet()

    def _ssh(self):
        ssh_command = 'ssh  -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -l {} {} -p {}'.format(self.username, self.hostname, self.port)
        self.handler = pexpect.spawn(ssh_command)
        self.expect(r"(?i)password[:]?\s*$")
        # s.expect("Password:")
        self.sendline(self.password)
        try:
            self.expect(r"[>#$]\s?",timeout=5)
        except pexpect.TIMEOUT:
            raise Exception("Device {} Login failed".format(self.hostname))
        self._terminal_length_zero()

    async def _ssh_async(self):
        ssh_command = 'ssh  -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -l {} {} -p {}'.format(self.username, self.hostname, self.port)
        self.handler = pexpect.spawn(ssh_command)
        await self.async_expect(r"(?i)password[:]?\s*$")
        # s.expect("Password:")
        self.sendline(self.password)
        try:
            await self.async_expect(r"[>|#|$]\s?",timeout=5)
        except pexpect.TIMEOUT:
            raise Exception("Device {} Login failed".format(self.hostname))
        self._terminal_length_zero()

    def _telnet(self):
        self.handler = pexpect.spawn('telnet {} {}'.format(self.hostname,self.port))
        self.sendline("\n")
        expect_user_list = []
        expect_user_list.append(r"[Uu]sername[:]?\s*")
        expect_user_list.append(r"[Ll]ogin[:]?\s*")
        expect_user_list.append(r"[>#\$]\s?")
        choice = self.expect(expect_user_list)
        if choice==2:
            self.sendline("end")
            self._terminal_length_zero()
            return
        self.sendline(self.username)
        self.expect(r"(?i)password[:]?\s*")
        self.sendline(self.password)
        try:
            self.expect(r"[>|#|$]\s?",timeout=5)
        except pexpect.TIMEOUT:
            raise Exception("Device {} Login failed".format(self.hostname))
        self._terminal_length_zero()

    async def _telnet_async(self):
        self.handler = pexpect.spawn('telnet {} {}'.format(self.hostname,self.port))
        self.sendline("\n")
        expect_user_list = []
        expect_user_list.append(r"[Uu]sername[:]?\s*")
        expect_user_list.append(r"[Ll]ogin[:]?\s*")
        expect_user_list.append(r"[>#$]\s?$")
        choice = await self.async_expect(expect_user_list)
        if choice==2:
            self.sendline("end")
            self._terminal_length_zero()
            return
        # self.sendline("\n")
        # await self.async_expect("Username:")
        self.sendline(self.username)
        await self.async_expect(r"(?i)password[:]?\s*")
        self.sendline(self.password)
        try:
            await self.async_expect(r"[>#$]\s?",timeout=5)
        except pexpect.TIMEOUT:
            raise Exception("Device {} Login failed".format(self.hostname))
        self._terminal_length_zero()


    def _terminal_length_zero(self):
        pass

    def run_commands(self,commands):
        while not self.handler:
            self._connect()
        if type(commands)==str:
            commands = [i.strip() for i in commands.split("\n") if i.strip()]
        elif type(commands)==list:
            pass
        else:
            raise Exception("Command invalid")
        try:
            return self._run_commands(commands)
        except pexpect.exceptions.EOF:
            try:
                self._connect()
                return self._run_commands(commands)
            except:
                raise Exception("Connection to {} is closed".format(self.hostname))

    async def async_run_commands(self,commands):
        while not self.handler:
            await self._async_connect()
        if type(commands) == str:
            commands = [i.strip() for i in commands.split("\n") if i.strip()]
        elif type(commands) == list:
            pass
        else:
            raise Exception("Command invalid")
        try:
            resp = await self._async_run_commands(commands)
            return resp
        except pexpect.exceptions.EOF:
            try:
                await self._connect()
                resp =await self._async_run_commands(commands)
                return resp
            except:
                raise Exception("Connection to {} is closed".format(self.hostname))


    def _run_commands(self,commands):
        pass

    async def _async_run_commands(self,commands):
        pass



    def configure(self,commands):
        while not self.handler:
            self._connect()
        if type(commands)==str:
            commands = [i.strip() for i in commands.split("\n") if i.strip()]
        elif type(commands)==list:
            pass
        else:
            raise Exception("Command invalid")
        return self._configure(self.run_commands,commands)

    async def async_configure(self,commands):
        while not self.handler:
            await self._async_connect()
        if type(commands)==str:
            commands = [i.strip() for i in commands.split("\n") if i.strip()]
        elif type(commands)==list:
            pass
        else:
            raise Exception("Command invalid")
        resp =await self._async_configure(self.async_run_commands,commands)
        return resp

    def _configure(self,func,commands):
        pass

    async def _async_configure(self,func,commands):
        pass
