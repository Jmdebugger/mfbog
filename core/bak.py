"""
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
"""


"""
url:http://app.50bang.org/?action=session

"""

r_app_key = "0307cafd710cab421a0310b134bd4e4c"  #come from AndroidManifest.xml
access = "4G"  #could be {WiFi ,unknown , 2G , 3G , 4G}
package = "com.sankuai.meituan" #apk包名
run_type = 4
project_name = "tongji_module"  #come from AndroidManifest.xml
uid = "866939020988806"   #代表手机用户id，具有唯一性，可以是imei,mac,或者随机数
brand = "hi6210sft"       #手机商标
promotion_method = "gf"   #come from AndroidManifest.xml
supplier = ""          #come from "META-INF/gysid_xxxx" or ""
app_version = "2.0"      #come from AndroidManifest.xml versionName
version_code = "200"     #come from AndroidManifest.xml versionCode
device_model = None      #Build.MODEL
os = "Android"           #常量
os_version = None        #Build.VERSION.RELEASE
resolution = "720*1280"  #手机分辨率
channel = "m-695326874"   #来源于META-INF/channel_XXX或者AndroidManifest.xml中的UMENG_CHANNEL
imei = "866939020988806"  #手机imei码
imsi = "#54352130550834"  #手机imsi码
wmac = "50a72b76c107"     #手机mac地址
toolcid = "gf"            #来源于com.market2345的SharedPreference文件.lminstalllist字段cid_key 或者AndroidManifest.xml中的UMENG_CHANNEL
android_id = None            #Settings$Secure.getString(context.getContentResolver(), "android_id");
total_time = None           #=SystemClock.elapsedRealtime() / 1000
sdk_version = "u1.0"        #常量
launch = ""                 #总为空