import nmap3
import json
import subprocess

nmap = nmap3.NmapScanTechniques()

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def validate_cidr(s):
        if s in range(30):
            return True
        else: 
            return False


def net_scan():
    
    net = input('IP: ') # 172.24.1.54
    
    cidr = input('CIDR: ') # /24
    
    if validate_ip(net):
        try:
            if validate_cidr(int(cidr)):

                net = f'{net}/{cidr}'
                results = nmap.nmap_ping_scan(net)

                a = json.dumps(results, indent=4)
                print(a)
                with open('result.json', 'w') as f:
                    f.write(a)
            else:
                print('Invalid CIDR try again!')
        except ValueError as e:
            print(e)
            net_scan()
    else:
        print('Invalid IP address try again!')



def port_scan():
    net = input('IP: ') # 172.24.1.54
    port = input('Port: ')
    
    cmd = f'nmap {net} -p{int(port)}'
    with open('result_port.txt', 'w') as f:
        return_code = subprocess.call(cmd, stdout=f)
        print(return_code)


def menu():
    with open(r'Module5\M5L4\menu.txt', 'r') as f:
        for x in f.readlines():
            print(x.strip())

    user_inp = input('>> ')
    if user_inp == '1':
        net_scan()
    elif user_inp == '2':
        port_scan()
    else:
        exit()

menu()