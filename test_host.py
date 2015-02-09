# !/user/bin/python
# -*- coding: utf-8 -*-
import time
import subprocess

def recconect():
    for ip in ip_list:
        ping = subprocess.call(["ping", ip])
        if ping == 0:
            time.sleep(30)
            print("UP") #rdectop reconect
            return ping
        else:
            time.sleep(5)
            recconect()

ip_list = ["Host"] #list of ip or domain name
while 1:
    for ip in ip_list:
        ping = subprocess.call(["ping", ip])
        if ping != 0:
            print("Down")
            recconect()
        else:
            print("Up")
            time.sleep(30)
