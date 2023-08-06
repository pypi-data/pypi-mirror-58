#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/22
# @time: 10:15
# @doc: 版本管理：由 Major.Minor.Patch 组成
# Copyright © 2019 natloc. All rights reserved.
#

from nat_lib.var_type import nat_string



# 判断是否合法的版本号
# return: bool
def isValid(vsnStr):
    vsnArr = vsnStr.split(".")

    if 3 != len(vsnArr):
        return False

    major = nat_string.trim(vsnArr[0])
    minor = nat_string.trim(vsnArr[1])
    patch = nat_string.trim(vsnArr[2])

    if not nat_string.isIntStr(major) or int(major) < 0:
        return False

    elif not nat_string.isIntStr(minor) or int(minor) < 0:
        return False

    elif not nat_string.isIntStr(patch) or int(patch) < 0:
        return False

    else:
        return True


# 转为版本号码
# return: string   # 如："10101"
def toCodeStr(vsnStr):
    if not isValid(vsnStr):
        return ""

    vsnArr = vsnStr.split(".")
    major = int(nat_string.trim(vsnArr[0]))
    minor = int(nat_string.trim(vsnArr[1]))
    patch = int(nat_string.trim(vsnArr[2]))

    return "%02d%02d%02d" %(major, minor, patch)