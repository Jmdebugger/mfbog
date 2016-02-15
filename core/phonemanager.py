#!/usr/bin/python
# -*- coding:utf-8 -*-
from spy import Spy
import glob

class PhoneManager(object):
    def __init__(self ,boss ,tid , name):
        self.boss = boss
        self.tid = tid
        self.name = name
        self.item = None
        self.phones = {}
        self.rootDIr = ("%s%d\\")%(glob.DbDir,self.tid)

    def fetchUnionApps(self):
        ret = Spy.getListForAndroid(self.tid)
        softlist = []
        if ret is not None:
            softlist = ret["softlist"]



    def generatePhone(self , phoneid):
        pass

    def onAdd(self):
        pass

    def onDel(self):
        pass

    def __unicode__(self):
        return u"%s[%s]"%(self.tid ,self.name)

