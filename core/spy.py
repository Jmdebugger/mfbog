#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import requests

import glob
import util
import json


class Spy(object):
    def __init__(self, phone):
        self.phone = phone
        pass

    @staticmethod
    def getListForAndroid(tid):
        headers = {'Accept': None,
                   'User-Agent': None}
        data = {
            "action": "getlist",
            "uid": tid,
            "returnType": "json",
            "sign": util.MyUtil.encrypt("{C8B22E37-AF95-4b84-9CCA-18A27D09D18B}",
                                        util.MyUtil.getMD5("getlist" + str(tid)))
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

    def action_sendData(self):
        headers = {'Accept': None,
                   'User-Agent': None}
        data = {
            "project":"tongji_module",
            "data": self.phone.uid,
            "sign":None
        }
        r = requests.post(glob.URL_ACTION_SENDDATA, data=data, headers=headers)
        if r.status_code ==200:
            ret = json.loads(r.text)
            if ret["status"] == True:
                return True
        return False



if __name__ == "__main__":

    print Spy.getListForAndroid(12345678)
