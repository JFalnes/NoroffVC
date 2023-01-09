from scapy.all import *
from scapy.layers.inet import Ether, TCP, IP, ICMP
from scapy.layers.l2 import ARP

ip_to_scan = '172.24.1.0/24'

ports = [80, 22, 23, 443]

def arp_scan(ip):

    request = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip)
    ans, unans = srp(request, timeout=2, retry=1)

    result = []
    for sent, received in ans:
        result.append({'IP': received.psrc, 'Mac':received.hwsrc})

    return result

def print_ports(port, state):
    print('%s | %s' % (port, state))

def syn_scan(target, ports):
    print('Syn scan on, %s wth ports %s' % (target, ports))
    sport = RandShort()
    for port in ports:
        pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags='S'), timeout=1, verbose=0)
        if pkt != None:
            if pkt.haslayer(TCP):
                if pkt[TCP].flags == 20:
                    print_ports(port, 'Closed')
                elif pkt[TCP].flags == 18:
                    print_ports(port, 'Open')
                else:
                    print_ports(port, 'TCP Packet response/filtered')
            elif pkt.haslayer(ICMP):
                print_ports(port, 'ICMP resp / filtered')
            else:
                print_ports(port, 'Unknown response')
                print(pkt.summary)
        else:
            print_ports(port, 'Unanswered')


result = arp_scan(ip_to_scan)

for x in range(len(result)):
    ip_dict = result[x]
    syn_scan(ip_dict['IP'], ports)