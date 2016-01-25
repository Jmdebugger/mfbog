#!/usr/bin/python
# -*- coding:utf-8 -*-
import httplib
import glob
import urllib2
import urllib

"""
urllib的用法参考http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html
"""
class Spy(object):
    def __init__(self , phone):
        self.phone = phone
        pass

    def getListForAndroid(self):
        header = {"User-Agent":"android"}
        """
        POST http://shouji.2345.com/api/getlist4android.php HTTP/1.1
        Content-Length: 95
        Content-Type: application/x-www-form-urlencoded
        Host: shouji.2345.com
        Connection: Keep-Alive

        action=getlist&uid=66666666&returnType=json&sign=UQ8HVABWUAYHVwFXCwICBQINAFRRWV1ZUwBdCF4DBwg%3D
        """

        data = {
            "action":"getlist",
            "uid":self.phone.uid,
            "returnType":"json",
            "sign":"UQ8HVABWUAYHVwFXCwICBQINAFRRWV1ZUwBdCF4DBwg%3D"
            #action=getlist&uid=68866988&returnType=json&sign=UQ8HVABWUAYHVwFXCwICBQINAFRRWV1ZUwBdCF4DBwg%3D
        }
        data = urllib.urlencode(data)
        print data
        req = urllib2.Request(glob.URL_GET_LIST_FOR_ANDROID,data ,header)
        resp = urllib2.urlopen(req)
        print req.headers
        print resp.headers
        content =  resp.read()
        print repr(content)




if __name__ == "__main__":
    import phone
    phone = phone.Phone(None)
    phone.uid = 68867988
    spy = Spy(phone)
    spy.getListForAndroid()


