#!/usr/bin/python
# -*- coding:utf-8 -*-
from phonemanager import PhoneManager
class Boss(object):
    def __init__(self , name):
        self.name = name
        self.item = None
        self.phoneManagers = {}

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def addPhoneManager(self , tid , name):
        if tid not in self.phoneManagers.keys():
            pm = PhoneManager(self ,tid , name)
            self.phoneManagers[tid] = pm
            pm.onAdd()
            return pm
        else:
            return self.phoneManagers[tid]

    def delPhoneManager(self ,tid):
        if tid in self.phoneManagers.keys():
            pm = self.phoneManagers.pop(tid)
            pm.onDel()
            return pm
        else:
            return None