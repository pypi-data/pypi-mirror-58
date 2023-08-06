#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 15:38
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import os
import sys
import shutil


from nat_lib.var_type import nat_string
from nat_lib.system import nat_cmd


# 获取绝对路径
# 注意：
#   若参数 path 以 / 开头：则绝对路径为 /...
#   否则：在 shell 路径后追加参数 path 字符串
def getAbsPath(path):
    argPath = nat_string.trim(path)
    if "" == argPath:
        return ""
    else:
        return os.path.abspath(argPath)

# 获取用户的 Home 目录地址
# return: string
def getUserHomePath():
    return nat_string.trim(nat_cmd.cmdRead("echo ~").read())


# 判断是否文件
def isFile(path):
    return os.path.isfile(getAbsPath(path))

# 判断是否合法的文件路径；不对该文件是否存在做判断
def isValidFilePath(file):
    absPath = getAbsPath(file)
    if "" == absPath:
        return False

    dirPath = os.path.dirname(absPath)
    filename = os.path.basename(absPath)
    (basename, suffixWithDot) = os.path.splitext(filename)

    # .xxx 文件
    if "" == suffixWithDot and basename == filename and len(filename) > 0 and "." == filename[0]:
        return isDir(dirPath)

    else:
       return isDir(dirPath) and "" != basename and len(suffixWithDot) > 1 and "." == suffixWithDot[0]

# 判断是否目录
def isDir(path):
    return os.path.isdir(getAbsPath(path))

# 判断是否存在；可能是 文档 或 目录
def isExist(path):
    return os.path.exists(getAbsPath(path))

# 列举指定目录下的 filename 列表
# return [string]
def listDir(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        return os.listdir(absPath)
    else:
        return []

# 创建目录
def mkDir(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        return True
    elif isExist(absPath):
        return False
    else:
        os.mkdir(absPath)
        return True

# 递归创建目录
def mkDirRecursive(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        return True
    elif isExist(absPath):
        return False
    else:
        os.makedirs(absPath)
        return True


# 删除指定的目录、及其内部所有档案
# return: bool
def rmDirRecursive(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        shutil.rmtree(absPath)
        return True
    else:
        return False

# 删除文件
def rmFile(path):
    absPath = getAbsPath(path)
    if isFile(absPath):
        os.remove(absPath)
        return True
    else:
        return False

# 拷贝目录
# return: bool
def cpDir(fromDir, toDir):
    fromDir = nat_string.trim(fromDir)
    toDir = nat_string.trim(toDir)

    return isDir(fromDir) and mkDirRecursive(toDir) and nat_cmd.cmd("cp -a %s %s" %(fromDir, toDir))


# 获取路径的目录
def getDirPath(path):
    absPath = getAbsPath(path)
    if isExist(absPath):
        return os.path.dirname(absPath)
    else:
        return ""



def isFilePlist(path):
    return __isTargetFile(path, "plist")

def isFilePng(path):
    return __isTargetFile(path, "png")

def isFileJpg(path):
    return __isTargetFile(path, "jpg") or __isTargetFile(path, "jpeg")

def __isTargetFile(path, suffix):
    return isFile(path) and (".%s" %(suffix)) == getFileSuffixWithDot(path).lower()




# 获取文件名
def getFilename(path):
    absPath = getAbsPath(path)
    if isExist(absPath):
        return os.path.basename(absPath)
    else:
        return ""

# 获取 basename
def getBasename(path):
    absPath = getAbsPath(path)
    if isFile(absPath):
        return os.path.splitext(absPath)[0]
    elif isDir(absPath):
        return os.path.basename(absPath)
    else:
        return ""

# 获取 suffix
def getFileSuffixWithDot(path):
    absPath = getAbsPath(path)
    if isFile(absPath):
        return os.path.splitext(absPath)[1]
    else:
        return ""

# 获取 suffix
def getFileSuffix(path):
    suffixWithDot = getFileSuffixWithDot(path)
    if "" == suffixWithDot:
        return ""
    elif "." == suffixWithDot[0] and len(suffixWithDot) > 1:
        return suffixWithDot[1:]
    else:
        return ""

# 拼接路径
def join(path1, path2):
    return os.path.join(path1, path2)

# 修改文件的 basename 部分
# return: bool
def rename(path, newBasename):
    absPath = getAbsPath(path)
    newBasename = nat_string.trim(newBasename)

    if "" == newBasename or not isExist(absPath):
        return False

    else:
        dirPath = getDirPath(absPath)
        suffixWithDot = getFileSuffixWithDot(absPath)
        newPath = join(dirPath, "%s%s" %(newBasename, suffixWithDot))
        os.rename(path, newPath)
        return True


# 获取当前路径：即当前 shell 所在的路径
def getCwd():
    return os.getcwd()

# 切换当前工作区目录
# return bool
def changeCwd(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        os.chdir(absPath)
        return True
    else:
        return False



# 获取脚本的包路径列表
# return [string]
def getScriptPathList():
    return sys.path

# 获取执行脚本所在的路径：即通过 python 命令直接执行的脚本所在的路径
def getExecScriptPath():
    list = getScriptPathList()
    if 0 == len(list):
        return ""
    else:
        return list[0]

# 插入脚本路径
# return bool
def insertScriptPath(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        if not hasContainScriptPath(absPath):
            sys.path.insert(0, path)

        return True
    else:
        return False

# 追加脚本路径
# return bool
def appendScriptPath(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        if not hasContainScriptPath(absPath):
            sys.path.append(path)

        return True
    else:
        return False

# 判断是否已包含了指定路径
def hasContainScriptPath(path):
    absPath = getAbsPath(path)
    if isDir(absPath):
        for p in getScriptPathList():
            if p == absPath:
                return True

    return False



