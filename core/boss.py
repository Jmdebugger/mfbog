#!/usr/bin/python
# -*- coding:utf-8 -*-
from phonemanager import PhoneManager
class Boss(object):
    def __init__(self , name):
        self.mName = name
        self.mPhoneManagers = {}

    def addPhoneManager(self , tid , name):
        if tid not in self.mPhoneManagers.keys():
            pm = PhoneManager(self ,tid , name)
            pm.onAdd()
            return pm
        else:
            return self.mPhoneManagers[tid]

    def delPhoneManager(self ,tid):
        if tid in self.mPhoneManagers.keys():
            pm = self.mPhoneManagers.pop(tid)
            pm.onDel()
            return pm
        else:
            return None