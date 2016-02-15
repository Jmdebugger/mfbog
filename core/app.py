#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import random
import threading
import time
import util
import requests
import urllib


class App(object):
    def __init__(self , phone):
        self.phone = phone
        self.total_time = 0

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
        self.channel = ""
        self.toolcid = ""

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
                  "channel":self.channel,
                  "supplier":self.supplier,
                  "promotion_method":self.promotion_method
                  }
        info = {"body":body , "header":header}
        return util.MyUtil.encrypt("0307cafd710cab421a0310b134bd4e4c", urllib.quote(json.dumps(info)))


    def action_sendData(self):
        headers = {'Accept': None,
                   'User-Agent': None}
        data = {
            "project":"tongji_module",
            "data": self._buildSelfStaticInfo(),
            "sign":None
        }
        r = requests.post(glob.URL_ACTION_SENDDATA, data=data, headers=headers)
        if r.status_code ==200:
            ret = json.loads(r.text)
            if ret["status"] == True:
                return True
        return False

    def getListForAndroid(self):
        headers = {'Accept': None,
                   'User-Agent': None}
        data = {
            "action": "getlist",
            "uid": self.phone.uid,
            "returnType": "json",
            "sign": util.MyUtil.encrypt("{C8B22E37-AF95-4b84-9CCA-18A27D09D18B}",
                                        util.MyUtil.getMD5("getlist" + str(self.phone.uid)))
        }
        r = requests.post(glob.URL_GET_LIST_FOR_ANDROID, data=data, headers=headers)
        if r.status_code == 200:
            try:
                ret = json.loads(r.text)
                if ret["errorCode"] == "0":
                    """
                    print ret["spreader_name"]  # FUTURE
                    print ret[
                        "groups"]  # 软件套餐[{u'packages': u'2;62;8;63;67;66;65;52;17;56;48;53;19;30;13;5;14;4', u'id': u'1', u'name': u'\u4e2d\u9ad8\u7aef\u673a\uff08\u517118\u6b3e\u8f6f\u4ef6\uff0c253.54MB\uff09'}]
                    softlist = ret[
                        "softlist"]  # 软件列表{u'iconpath': u'http://shouji.2345.com/shoujiimg/img/resource/article/baoku.jpg', u'url': u'http://sj3.2345.cn/baoku/12345678', u'packagename': u'com.market2345', u'description': u'\u4f60\u60f3\u8981\u7684\uff0c\u624b\u673a\u52a9\u624b\u90fd\u6709', u'softname': u'\u738b\u724c\u624b\u673a\u52a9\u624b', u'versionName': u'V3.4.2', u'bakUrl': u'http://ttff8.2345.cn/baoku/12345678', u'versionCode': u'46', u'id': u'3', u'size': u'6.68MB'}
                    for i in range(0, len(softlist)):
                        print softlist[i]
                """
                return ret
            except Exception, e:
                print "getListForAndroid:" + str(e)
        return None

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



