#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 11:57
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

from nat_lib.log    import nat_console
from nat_lib.system import nat_cmd
from nat_lib.var_type import nat_string



# 获取当前差异内容
# return string
def status_retStr():
    ret = nat_cmd.cmdRead("git status")

    if nat_cmd.isLastCmdSuccess():
        return ret.read()
    else:
        return ""

# 是否已提交完所有变更
# return: bool
def status_isClean():
    return status_retStr().find("nothing to commit, working tree clean") >= 0



# 下载代码
# return: bool
def clone(url):
    url = nat_string.trim(url)
    if "" != url:
        return nat_cmd.cmd("git clone %s" %(url))
    else:
        return False

# 刷新
# return: bool
def fetch():
    return nat_cmd.cmd("git fetch")

# 更新代码
# return: bool
def pull(branchName = "master", repoName = "origin", enableEdit = True):
    branchName = nat_string.trim(branchName)
    repoName = nat_string.trim(repoName)

    if "" == branchName or "" == repoName:
        return False
    else:
        editMode = ""
        if not enableEdit:
            editMode = "--no-edit"
        return nat_cmd.cmd("git pull %s %s %s" %(repoName, branchName, editMode))


# 添加所有修改
# return: bool
def add():
    return nat_cmd.cmd("git add .")



# 提交
# return: bool
def commit(messageStr):
    nat_cmd.cmd(u"git commit -m \"%s\"" %(messageStr))

# 添加并提交
# return: bool
def addAndCommit(messageStr):
    return add() and commit(messageStr)


# 推送代码
# return: bool
def push(branchName = "master", repoName = "origin", withTags = False):
    branchName = nat_string.trim(branchName)
    repoName = nat_string.trim(repoName)

    if "" == branchName or "" == repoName:
        return False
    else:
        if withTags:
            withTagsStr = "--tags"
        else:
            withTagsStr = ""

        return nat_cmd.cmd("git push %s %s %s" %(repoName, branchName, withTagsStr))





# 获取所有分支列表
# return: [string]
def branch_list():
    ret = nat_cmd.cmdRead("git branch")

    branchList = []
    if nat_cmd.isLastCmdSuccess():
        for line in ret.readlines():
            branch = line.lstrip("*").strip()
            if "" != branch:
                branchList.append(branch)


    return branchList

# 获取当前分支名
# return: string
def branch_current():
    ret = nat_cmd.cmdRead("git branch")

    if nat_cmd.isLastCmdSuccess():
        for line in ret.readlines():
            if 0 == line.find("* "):
                return line.lstrip("*").strip()

    return ""

# 判断当前是否主分支
# return: bool
def branch_isCurMaster():
    return "master" == branch_current()

# 判断是否有指定的分支
# return: bool
def branch_hasBranch(branchNameStr):
    for branch in branch_list():
        if branch == branchNameStr:
            return True

    return False

# 切换分支；如果目标分支不存在则返回 false
# return bool
def branch_switch(branchNameStr):
    if branch_hasBranch(branchNameStr):

        if branch_current() == branchNameStr:
            return True
        else:
            nat_cmd.cmd(u"git checkout %s" %(branchNameStr))
            return branch_current() == branchNameStr

    else:
        return False

# 切换分支；如果目标分支不存在则自动创建
# # return bool
def branch_switchSafety(branchNameStr):
    if branch_switch(branchNameStr):
        return True

    branchNameStr = nat_string.trim(branchNameStr)
    if "" != branchNameStr and nat_cmd.cmd(u"git checkout -b %s" %(branchNameStr)):
        return True

    else:
        return False



# 添加 tag 名
# return: bool
def tag_add(tagNameStr):
    tagNameStr = nat_string.trim(tagNameStr)
    if "" == tagNameStr:
        return False
    else:
        return nat_cmd.cmd("git tag %s" %(tagNameStr))

# 移除 tag 名
# return: bool
def tag_remove(tagNameStr):
    tagNameStr = nat_string.trim(tagNameStr)
    if "" == tagNameStr:
        return False
    else:
        return nat_cmd.cmd("git tag -d %s" %(tagNameStr))








