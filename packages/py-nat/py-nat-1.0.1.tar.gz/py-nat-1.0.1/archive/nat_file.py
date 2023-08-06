#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 13:45
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import base64
import hashlib


from nat_lib.archive import nat_path



# 获取文件的 base64
# return: string
def getBase64(path):
    if nat_path.isFile(path):
        fp = open(nat_path.getAbsPath(path), "r")
        base64Str = base64.b64encode(fp.read())
        fp.close()
        return base64Str

    else:
        return ""


# 获取文件的 md5
# return: string
def getMd5(path):
    if nat_path.isFile(path):
        hash = hashlib.md5()
        fp = open(nat_path.getAbsPath(path), "r")

        while True:
            b = fp.read(8096)
            if not b:
                break
            hash.update(b)

        fp.close()
        return hash.hexdigest()

    else:
        return ""


# 读取文件内容
# return: string
def read(path):
    if nat_path.isFile(path):
        fp = open(nat_path.getAbsPath(path), "r")
        content = fp.read()
        fp.close()
        return content

    else:
        return ""

# 创建空文件
# return: bool
def createEmptyFile(file, contentStr = ""):
    if nat_path.isValidFilePath(file) and not nat_path.isFile(file):
        fp = open(file, "w")
        fp.write(contentStr)
        fp.close()
        return True
    else:
        return False

# 写数据到文件；若文件不存在则新建
# return: bool
def write(dir, filename, contentStr = ""):
    if not nat_path.isDir(dir):
        return False

    elif not nat_path.isValidFilePath(nat_path.join(dir, filename)):
        return False

    else:
        path = nat_path.join(dir, filename)
        fp = open(path, "w")
        fp.write(contentStr)
        fp.close()
        return True
