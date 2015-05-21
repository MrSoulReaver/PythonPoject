# !/user/bin/python
# -*- coding: utf-8 -*-
import time
import subprocess

def recconect():
    for ip in ip_list:
        ping = subprocess.call([u"ping", ip])
        if ping == 0:
            time.sleep(30)
            print(u"UP") #rdectop reconect
            return ping
        else:
            time.sleep(5)
            recconect()

ip_list = [u"8.8.8.8"] #list of ip or domain name
while 1:
    for ip in ip_list:
        ping = subprocess.call([u"ping", ip])
        if ping != 0:
            print(u"Down")
            recconect()
        else:
            print(u"Up")
            time.sleep(30)
