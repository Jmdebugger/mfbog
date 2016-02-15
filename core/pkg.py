#!/usr/bin/python
# -*- coding:utf-8 -*-
import glob
import core
class Package:
    def __init__(self):
        self.iconpath = None
        self.url = None
        self.packagename = None
        self.description = None
        self.softname = None
        self.versionName = None
        self.bakUrl = None
        self.versionCode = None
        self.id = None
        self.size = None
        self.hasNewVersion = True
        self.bDownloaded = False

    def download(self):
        pass






class PackageManager:
    def __init__(self , pm):
        self.pm = pm
        self.rootDir = u"%s%d"%(glob.DbDir , pm.tid)
        self.packages = {}

    def __parse(self ,soft):
        package = Package()
        for key in soft.keys():
            exec("package.%s = '%s'"%(key,soft[key]))   #哈哈哈，故意的
        print vars(package)
        return package



    def update(self):
        ret = core.Spy.getListForAndroid(self.pm.tid)
        if ret is not None:
            softlist = ret["softlist"]
            for soft in softlist:
                if self.packages.has_key(soft["packagename"]):
                    package = self.packages[soft["packagename"]]
                    if package.versionCode < soft["versionCode"]:
                        package.hasNewVersion = True

                else:
                    package = self.__parse(soft)
                    self.packages[soft["packagename"]] = package
                    self.bDownloaded = False



if __name__ == "__main__":
    pm = core.PhoneManager(None , 12345678 , "sss")
    PackageManager(pm).update()









