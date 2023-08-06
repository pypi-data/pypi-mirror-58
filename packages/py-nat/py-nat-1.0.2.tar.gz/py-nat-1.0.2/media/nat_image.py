#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019-10-18
# @time: 22:50
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

from nat_lib.system import nat_cmd
from nat_lib.log import nat_console


cmdPillow = "Pillow"
if not nat_cmd.hasInstalledPipCmd(cmdPillow) and not nat_cmd.installPipCmd(cmdPillow, True):
    nat_console.error(u"安装 %s 失败" %(cmdPillow))


from PIL import Image
from nat_lib.archive import nat_path
from nat_lib.var_type import nat_string



class NatImage:

    __img = None
    __imgFile = ""

    def __init__(self, imgFile):
        imgFile = nat_path.getAbsPath(imgFile)
        if nat_path.isFile(imgFile):
            self.__img = Image.open(imgFile)

        self.__imgFile = imgFile
        if None == self.__img:
            nat_console.error(u"加载图片文件失败: %s" %(imgFile))


    # 判断是否有效的图片
    def isAvail(self):
        return None != self.__img

    # 获取图像
    def getImg(self):
        return self.__img


    # 获取宽度
    # return: int
    def getWidth(self):
        return self.__img.size[0]

    # 获取高度
    # return: int
    def getHeight(self):
        return self.__img.size[1]


    # 设置宽度
    # return: bool
    def setWidth(self, widthInt, isAspect = False):
        if widthInt <= 0:
            return False

        elif self.getWidth() == widthInt:
            if isAspect:
                return self.setHeight(widthInt)
            else:
                return True

        else:
            heightInt = self.getHeight()
            self.__img = self.__img.resize((widthInt, heightInt))

            if isAspect:
                return self.setHeight(widthInt)
            else:
                return True

    # 设置高度
    # return: bool
    def setHeight(self, heightInt, isAspect = False):
        if heightInt <= 0:
            return False

        elif self.getHeight() == heightInt:
            if isAspect:
                return self.setWidth(heightInt)
            else:
                return True

        else:
            widthInt = self.getWidth()
            self.__img = self.__img.resize((widthInt, heightInt))

            if isAspect:
                return self.setWidth(heightInt)
            else:
                return True


    # 开启颜色模式
    def setRGBA(self):
        if None != self.__img:
            self.__img = self.__img.convert("RGBA")

        return self


    # 在当前图片上粘贴另一张图片
    def pasteImg(self, aboveImg, offsetX = 0, offsetY = 0):
        if None != aboveImg and aboveImg.isAvail() and self.isAvail():
            self.__img.paste(aboveImg.getImg(), (offsetX, offsetY))

        return self

    # 保存图片：覆盖自身
    # return: bool
    def save(self):
        filename = nat_path.getFilename(self.__imgFile)
        return self.saveWithNewName(filename)

    # 保存图片：新图片所在的路径与源图片相同
    # return: bool
    def saveWithNewName(self, newFilename):
        newFilename = nat_string.trim(newFilename)
        if "" == newFilename:
            return False

        dir = nat_path.getDirPath(self.__imgFile)
        newPath = nat_path.join(dir, newFilename)
        return self.saveWithNewPath(newPath)

    # 保存图片到新目录
    # return: bool
    def saveWithNewDir(self, newDir):
        newDir = nat_string.trim(newDir)
        if not nat_path.isDir(newDir) and not nat_path.mkDirRecursive(newDir):
            return False

        filename = nat_path.getFilename()
        newPath = nat_path.join(newDir, filename)
        return self.saveWithNewPath(newPath)

    # 保存图片到新路径
    # return: bool
    def saveWithNewPath(self, newPath):
        newPath = nat_string.trim(newPath)
        if not nat_path.isValidFilePath(newPath):
            return False
        else:
            self.__img.save(newPath)
            return True












