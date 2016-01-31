#!/usr/bin/python
# -*- coding:utf-8 -*-
import threading
class Phone(threading.Thread):
    def __init__(self ,phoneManager):
        self.imei = None
        self.imsi = None
        self.wmac = None
        self.os = "Android"
        self.resolution = None
        self.access = None
        self.os_version = None
        self.android_id = None
        self.uid = None
        self.total_time = None


    def installApp(app):
        pass

    def uninstallApp(app):
        pass

    def poweron(self):
        pass
    def poweroff(self):
        pass






if __name__ == "__main__":
    #phone = PhoneManager.randomGenPhone()
    pass
    #print vars(phone)
    
