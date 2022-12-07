import os
import threading


def list_func():
    host_ip = input('IP to scan: ')
    my_list = []

    for x in range(255):
       a = host_ip.split('.')
       a[3] = str(x)
       a = '.'.join(a)
       
       my_list.append(a)

    return my_list

def scan(host):

    response = os.popen(f"ping -c 1 {host}").read()
    if 'timed out' in response or 'unreachable' in response:
        pass
    else:
        print(f"Host is up: {host} \nStatus: Ping Successful")

for x in list_func():
    t1 = threading.Thread(target=scan, args=(x,))
    t1.start()

