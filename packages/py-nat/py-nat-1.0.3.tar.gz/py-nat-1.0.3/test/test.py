#!/usr/local/bin/python3


import nat.string
import nat.cmd

print(nat.string.trim(" ha ha     "))

print(nat.cmd.execRead("ls -l").read())

print(nat.cmd.isPythonVsn2())
print(nat.cmd.isPythonVsn3())
print(nat.cmd.getPythonVsn())

print(nat.cmd.hasCmd("pod"))


import thd.wechat.group_robot

# webHook = ""
# msg = thd.wechat.group_robot.TextMessage(webHook)
# msg.send()