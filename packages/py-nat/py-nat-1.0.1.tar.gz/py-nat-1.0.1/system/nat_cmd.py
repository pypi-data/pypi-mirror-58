#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 13:19
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import os
import platform

from nat_lib.log import nat_console
from nat_lib.var_type import nat_string




# 获取当前 Python 的版本
# return: string   # 如："2.7.5"
def getPythonVsn():
    return platform.python_version()

# 判断当前是否 Python 2.x
# return: bool
def isPythonVsn2():
    return "2" == getPythonVsn().split(".")[0]

# 判断当前是否 Python 3.x
# return: bool
def isPythonVsn3():
    return "3" == getPythonVsn().split(".")[0]



# 执行命令
# return int   # 0-成功
def cmd(cmdStr):
    return 0 == os.system(cmdStr)

def cmdRead(cmdStr):
    return os.popen(cmdStr)



# 判断是否已安装命令
# return: bool
def hasCmd(commandStr):
    commandStr = nat_string.trim(commandStr)
    if "" == commandStr:
        return False
    else:
        return cmd("which %s" %(commandStr))

# 安装 pip 命令
# return true
def installPip():
    cmdStr = "sudo easy_install pip"
    return cmd(cmdStr)

# pip 安装命令工具
# return bool
def installPipCmd(commandStr, withSudo = False):
    if hasCmd(commandStr):
        return True

    elif isPythonVsn3():
        return __installPipCmd("pip3", commandStr, withSudo)

    elif isPythonVsn2():
        return __installPipCmd("pip", commandStr, withSudo)

    else:
        nat_console.error(u"请先安装 pip 命令")
        return False

def __installPipCmd(pipCmd, commandStr, withSudo):
    if withSudo:
        sudoStr = "sudo "
    else:
        sudoStr = ""

    cmdStr = "%s%s install %s" %(sudoStr, pipCmd, commandStr)
    isSuccess = cmd(cmdStr)

    if not isSuccess:
        nat_console.error(u"%s 安装命令 %s 失败！" %(pipCmd, commandStr))
    return isSuccess

# 判断是否已通过 pip 安装命令
# return: bool
def hasInstalledPipCmd(commandStr):
    commandStr = nat_string.trim(commandStr)
    if "" == commandStr:
        return False
    else:
        return "" != cmdRead("pip show %s" %(commandStr)).read()




# 获取上一条命令执行的返回码
# @return code :: int   # 0-成功；

def getLastCmdRetCode():
    return int(cmdRead("echo $?").read().strip())

# 判断上一条命令是否执行成功

def isLastCmdSuccess():
    return 0 == getLastCmdRetCode()
    



