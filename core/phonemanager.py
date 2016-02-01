#!/usr/bin/python
# -*- coding:utf-8 -*-

class PhoneManager(object):
    def __init__(self ,boss ,tid , name):
        self.boss = boss
        self.tid = tid
        self.name = name
        self.item = None
        self.phones = {}

    def installAppsToPhone(self ,phone , apps):
        pass

    def generatePhone(self , phoneid):
        pass

    def onAdd(self):
        pass

    def onDel(self):
        pass

    def __unicode__(self):
        return u"%s[%s]"%(self.tid ,self.name)

