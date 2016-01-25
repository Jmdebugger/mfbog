# -*- coding:utf-8 -*-
import socket
import struct
CMD_TYPE_HEARTBEAT = 502
CMD_TYPE_GET_PHONE_INFO = 301
CMD_TYPE_GET_MORE_PHONE_INFO = 29
CMD_TYPE_GET_SERVER_APP_NAME = 309
CMD_TYPE_START_TWINKLE_ACTIVITY = 500


def sendHeartbeat(s):
    packet = struct.pack("II" , CMD_TYPE_HEARTBEAT , 0)
    s.send(packet)

def getPhoneInfo(s):
    packet = struct.pack("II" , CMD_TYPE_GET_PHONE_INFO , 0)
    s.send(packet)
    print repr(s.recv(1024))

def getMorePhoneInfo(s):
    packet = struct.pack("II" , CMD_TYPE_GET_MORE_PHONE_INFO , 0)
    s.send(packet)
    print repr(s.recv(1024))

def startTwinkleActivity(s):
    packet = struct.pack("II" , CMD_TYPE_START_TWINKLE_ACTIVITY , 0)
    s.send(packet)


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect(("127.0.0.1" , 11479))
    #sendHeartbeat(s)
    #getMorePhoneInfo(s)
    startTwinkleActivity(s)
    s.close()
