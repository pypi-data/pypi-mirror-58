#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019-10-16
# @time: 01:06
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import urllib2

from nat_lib.var_type import nat_string



# 请求 url 的数据
# return: string
def reqUrl(urlStr):
    urlStr = nat_string.trim(urlStr)
    if "" != urlStr:
        req = urllib2.Request(urlStr)
        resp = urllib2.urlopen(req)
        return resp.read()

    else:
        return ""
