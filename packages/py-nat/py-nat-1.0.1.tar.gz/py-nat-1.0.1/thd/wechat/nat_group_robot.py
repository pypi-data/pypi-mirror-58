#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 11:20
# @doc: 企业微信群机器人
# Copyright © 2019 natloc. All rights reserved.
#
# 文档：https://work.weixin.qq.com/api/doc?notreplace=true&version=2.8.10.6069&platform=mac#90000/90136/91770
#

from nat_lib.archive import nat_path
from nat_lib.archive import nat_file
from nat_lib.system import nat_cmd
from nat_lib.var_type import nat_string, nat_json
from nat_lib.log import nat_console


# 基础消息
class __Message(object):

    __HTTP_HEADER_CONTENT_TYPE = "Content-Type: application/json"
    _ERROR_MSG_PREFIX = u"企业微信群机器人 * "

    # 机器人的地址
    __webHookUrl = ""


    def __init__(self, webHookUrl):
        self.__webHookUrl = nat_string.trim(webHookUrl)

        if "" == self.__webHookUrl:
            nat_console.error(u"%s实例化失败：机器人的 webhook 地址为空字符串" %(self._ERROR_MSG_PREFIX))


    # 发送消息
    # param: msgType :: string
    # param: jsonData :: json
    # return: bool
    def _send(self, msgType, jsonDict):
        argMsgType = nat_string.trim(msgType)

        if "" == self.__webHookUrl:
            nat_console.error(u"%s发送消息失败：机器人的 webhook 地址为空字符串" %(self._ERROR_MSG_PREFIX))
            return False

        elif "" == argMsgType:
            nat_console.error(u"%s发送消息失败：消息类型错误" %(self._ERROR_MSG_PREFIX))
            return False

        elif not isinstance(jsonDict, dict):
            nat_console.error(u"%s发送消息失败：消息内容类型错误" %(self._ERROR_MSG_PREFIX))
            return False

        else:
            msgJson = {}
            msgJson["msgtype"] = msgType
            msgJson[msgType] = jsonDict

            jsonStr = nat_json.json2str(msgJson)
            cmdStr = "curl %s -H '%s' -d '%s'" %(self.__webHookUrl, self.__HTTP_HEADER_CONTENT_TYPE, jsonStr)
            return nat_cmd.cmd(cmdStr)



# text 消息
class TextMessage(__Message):

    __KEY_CONTENT = "content"
    __KEY_MENTIONED_LIST = "mentioned_list"
    __KEY_MENTIONED_MOBILE_LIST = "mentioned_mobile_list"

    # 消息数据
    __msgJson = {}


    # 设置消息内容
    def setContent(self, contentStr):
        self.__msgJson[self.__KEY_CONTENT] = nat_string.trim(contentStr)


    # 设置提醒所有人
    def setMentionedAll(self):
        self.__msgJson[self.__KEY_MENTIONED_LIST] = ["@all"]
        self.__msgJson[self.__KEY_MENTIONED_MOBILE_LIST] = []


    # 追加提醒人的 ID
    # param: userId :: string   # 如："lilei"
    # return: bool
    def appendMentionedUser(self, userId):
        argUserId = nat_string.trim(userId)
        if "" == argUserId:
            nat_console.error(u"%s添加提醒人的 ID 失败：用户 ID 为空字符串" %(self._ERROR_MSG_PREFIX))
            return False

        else:
            mentionedList = self.__msgJson.get(self.__KEY_MENTIONED_LIST, [])

            if 1 == len(mentionedList) and "@all" == mentionedList[0]:
                mentionedList = []

            for uid in mentionedList:
                if uid == argUserId:
                    return True

            mentionedList.append(argUserId)
            self.__msgJson[self.__KEY_MENTIONED_LIST] = mentionedList

            return True


    # 追加提醒人的 手机号
    # return: bool
    def appendMentionedPhone(self, phoneNumStr):
        argPhoneNumStr = nat_string.trim(phoneNumStr)
        if 11 != len(argPhoneNumStr):
            nat_console.error(u"%s添加提醒人的 手机号 失败：手机号不合法 %s" %(self._ERROR_MSG_PREFIX, argPhoneNumStr))
            return False

        else:
            mentionedList = self.__msgJson.get(self.__KEY_MENTIONED_LIST, [])
            if 1 == len(mentionedList) and "@all" == mentionedList[0]:
                self.__msgJson[self.__KEY_MENTIONED_LIST] = []


            mentionedMobileList = self.__msgJson.get(self.__KEY_MENTIONED_MOBILE_LIST, [])
            for phone in mentionedMobileList:
                if phone == argPhoneNumStr:
                    return True

            mentionedMobileList.append(argPhoneNumStr)

            self.__msgJson[self.__KEY_MENTIONED_MOBILE_LIST] = mentionedMobileList

            return True


    # 发送消息
    # return: bool
    def send(self):
        contentStr = self.__msgJson.get(self.__KEY_CONTENT, "").strip()
        mentionedUserIdList = self.__msgJson.get(self.__KEY_MENTIONED_LIST, [])
        mentionedPhoneList = self.__msgJson.get(self.__KEY_MENTIONED_MOBILE_LIST, [])
        if "" == contentStr and [] == mentionedPhoneList and [] == mentionedUserIdList:
            nat_console.warn(u"%s发送消息失败：取消发送无意义的内容" %(self._ERROR_MSG_PREFIX))
            return

        else:
            return self._send("text", self.__msgJson)



# markdown 消息
class MarkdownMessage(__Message):

    __KEY_CONTENT = "content"
    __DEFAULT_HEAD_SIZE = 3

    # 消息数据
    __msgJson = {}

    # 内容文本
    __content = ""



    # 设置链接
    def mkLink(self, contentStr, urlStr):
        argContentStr = nat_string.trim(contentStr)
        argUrlStr = nat_string.trim(urlStr)

        if "" == argContentStr:
            return ""

        elif "" == argUrlStr:
            return contentStr

        else:
            return u"[%s](%s)" %(argContentStr, argUrlStr)



    # 设置引用
    # return string
    def mkQuote(self, contentStr):
        if "" == contentStr:
            return ""
        else:
            return u"> %s" %(contentStr)



    # 添加绿色文本
    # return: string
    def mkColorGreen(self, contentStr):
        return self.__mkTextColor("info", contentStr)

    # 添加橙色文本
    # return: string
    def mkColorOrange(self, contentStr):
        return self.__mkTextColor("warning", contentStr)

    # 添加灰色文本
    # return: string
    def mkColorGray(self, contentStr):
        return self.__mkTextColor("comment", contentStr)

    # return: string
    def __mkTextColor(self, typeStr, contentStr):
        if "" == contentStr:
            return ""
        else:
            return u"<font color=\"%s\">%s</font>" %(typeStr, contentStr)



    # 生成行字符串
    # param: headSize :: int   # 尺寸：取值范围：[0, 6]；值越大字体越小；默认值：3；0-不使用
    # return: string
    def mkLine(self, contentStr, headSize = 0, isBold = False, newLine = True):
        argContentStr = nat_string.trim(contentStr)
        if "" == argContentStr:
            return ""

        else:
            argSize = headSize
            if not isinstance(headSize, int) or argSize < 0 or argSize > 6:
                argSize = self.__DEFAULT_HEAD_SIZE

            prefix = ""
            if argSize > 0:
                for _ in range(0, argSize):
                    prefix += "#"

                prefix += " "

            argContentStr = self.__mkBoldStr(argContentStr, isBold)
            argContentStr = u"%s%s" %(prefix, argContentStr)
            return self.__mkNewLineStr(argContentStr, newLine)



    # 添加行；末尾添加换行符
    # return: bool
    def append(self, contentStr):
        if nat_string.isStr(contentStr):
            self.__content += contentStr
            return True

        else:
            return False



    def __mkNewLineStr(self, contentStr, newLine):
        if newLine:
            return u"%s\n" %(contentStr)
        else:
            return contentStr

    def __mkBoldStr(self, contentStr, isBold):
        if isBold:
            return u"**%s**" %(contentStr)
        else:
            return contentStr


    # 发送消息
    # return: bool
    def send(self):
        contentStr = nat_string.trim(self.__content)
        if "" == contentStr:
            nat_console.warn(u"%s发送 md 消息失败：取消发送无意义的内容" %(self._ERROR_MSG_PREFIX))
            return

        else:
            self.__msgJson[self.__KEY_CONTENT] = contentStr
            return self._send("markdown", self.__msgJson)



# image 消息
class ImageMessage(__Message):

    __KEY_BASE_64 = "base64"
    __KEY_MD_5 = "md5"

    # 消息数据
    __msgJson = {}

    # 要发送的图片地址
    __imgPath = ""


    # 设置图片；仅支持 png | jpg 格式，且 <= 2M
    # return: bool
    def setImg(self, path):
        if not nat_path.isFile(path):
            nat_console.error(u"%s设置图片失败：文件不存在：%s" %(self._ERROR_MSG_PREFIX, path))
            return False

        suffixWithDot = nat_path.getFileSuffixWithDot(path)
        if ".png" != suffixWithDot and ".jpg" != suffixWithDot and ".jpeg" != suffixWithDot:
            nat_console.error(u"%s设置图片失败：不支持的图片格式：%s" %(self._ERROR_MSG_PREFIX, suffixWithDot))
            return False

        self.__imgPath = nat_path.getAbsPath(path)
        return True


    # 发送消息
    # return: bool
    def send(self):
        if not nat_path.isFile(self.__imgPath):
            nat_console.warn(u"%s发送消息失败：未设置要发送的图片" %(self._ERROR_MSG_PREFIX))
            return False


        base64Str = nat_file.getBase64(self.__imgPath)
        md5Str = nat_file.getMd5(self.__imgPath)
        if "" == base64Str or "" == md5Str:
            nat_console.warn(u"%s发送消息失败：图片解析失败" %(self._ERROR_MSG_PREFIX))
            return

        else:
            self.__msgJson[self.__KEY_BASE_64] = base64Str
            self.__msgJson[self.__KEY_MD_5] = md5Str
            return self._send("image", self.__msgJson)



# news 消息
class NewsMessage(__Message):

    __KEY_ARTICLES = "articles"
    __KEY_TITLE = "title"
    __KEY_DESC = "description"
    __KEY_URL = "url"
    __KEY_PIC_URL = "picurl"


    # 消息数据
    __msgJson = {}

    __MAX_NEWS_COUNT = 8


    # 添加一条新闻
    def appendNews(self, title, desc, url, picUrl):
        newsList = self.__msgJson.get(self.__KEY_ARTICLES, [])

        if len(newsList) >= self.__MAX_NEWS_COUNT:
            nat_console.error(u"%s添加新闻消息失败：已达最大新闻数量" %(self._ERROR_MSG_PREFIX))
            return False

        argTitle = nat_string.trim(title)
        argDesc = nat_string.trim(desc)
        argUrl = nat_string.trim(url)
        argPicUrl = nat_string.trim(picUrl)

        if "" == argTitle:
            nat_console.error(u"%s添加新闻消息失败：标题为空，链接：%s" %(self._ERROR_MSG_PREFIX, argUrl))
            return False
        elif "" == argUrl:
            nat_console.error(u"%s添加新闻消息失败：链接为空，标题：%s" %(self._ERROR_MSG_PREFIX, argTitle))
            return False
        else:
            news = {}
            news[self.__KEY_TITLE] = argTitle
            news[self.__KEY_DESC] = argDesc
            news[self.__KEY_URL] = argUrl
            news[self.__KEY_PIC_URL] = argPicUrl

            newsList.append(news)
            self.__msgJson[self.__KEY_ARTICLES] = newsList
            return True


    # 发送消息
    # return: bool
    def send(self):
        if 0 == len(self.__msgJson.get(self.__KEY_ARTICLES, [])):
            nat_console.warn(u"%s发送 md 消息失败：取消发送无意义的内容" %(self._ERROR_MSG_PREFIX))
            return

        else:
            return self._send("news", self.__msgJson)












