#!/usr/bin/python
# -*- coding:utf-8 -*-
import myutil
import glob
import json
import threading
import time
import random

class App(object):
    def __init__(self , phone):
        self.phone = phone

    def _buildSelfStaticInfo(self):
        pass

    def run(self):
        pass

    def exit(self):
        pass

class AppUsbHelper(App):
    def __init__(self , phone):
        super(AppUsbHelper ,self).__init__(phone)
        self.total_time = 848
        self.package = "com.service.usbhelper"
        self.project_name = "tongji_module"
        self.sdk_version = "u1.0"
        self.app_version = "2.0"
        self.run_type = 4
        self.src_package = "com.market2345"
        self.version_code = "200"
        self.supplier = ""
        self.promotion_method = "gf"
        self.launch = ""

    def _buildSelfStaticInfo(self):
        body = {"launch":self.launch}
        header = {"total_time":self.total_time,
                  "uid":self.phone.uid,
                  "os":self.phone.os,
                  "project_name":self.project_name,
                  "package":self.package,
                  "sdk_version":self.sdk_version,
                  "app_version":self.app_version,
                  "run_type":self.run_type,
                  "resolution":self.phone.resolution,
                  "src_package":self.src_package,
                  "access":self.phone.access,
                  "os_version":self.phone.os_version,
                  "version_code":self.version_code,
                  "local_id":{"wmac":self.phone.wmac,"imsi":self.phone.imsi,"imei":self.phone.imei},
                  "android_id":self.phone.android_id,
                  "device_model":"Coolpad 8707",
                  "brand":"Coolpad",
                  "toolcid":self.phone.toolcid,
                  "channel":self.phone.channel,
                  "supplier":self.supplier,
                  "promotion_method":self.promotion_method
                  }
        info = {"body":body , "header":header}
        return json.dumps(info)

class AppManager(threading.Thread):

    def __init__(self ,phone,interval = 2):
        self.phone = phone
        self.apps = {}
        self.interval = interval
        self.running = True

    def run(self):
        while self.running:
            if len(self.apps.keys()) == 0:
                continue
            r = random.randint(0 , 1)
            i = random.randint(0 , len(self.apps.keys()))
            if r == 1:
                app_id = self.apps.keys()[i]
                self.apps[app_id].run()
            time.sleep(self.interval)

    def stop(self):
        self.running = False

    def installApp(self , app):
        if not self.apps.has_key(app.id):
            self.apps[app.app_id] = app

    def uninstallApp(self , app_id):
        if self.apps.has_key(app_id):
            self.apps.pop(app_id)






if __name__ =="__main__":
    print threading.currentThread().getName()
    from phone import Phone
    phone = Phone()
    phone.imei = "111"
    phone.imsi = "222"
    phone.wmac = "333"
    phone.uid = "5654444"
    phone.os = "Android"
    phone.resolution = "rrr"
    phone.access = "wifi"
    phone.os_version = "4.4.2"
    phone.android_id = "android_idxxx"
    phone.toolcid = "sddd"
    phone.channel = "gf"
    app = AppUsbHelper(phone)
    appman = AppManager(phone)
    print app._buildSelfStaticInfo()
    import sys
    sys.stdin.read()



