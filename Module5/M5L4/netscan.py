import nmap3
import json
net = input('IP: ') # 192.268.0.0/24

nmap = nmap3.NmapScanTechniques()

def scan(nmap):
    results = nmap.nmap_ping_scan(net)
    print(json.dumps(results, indent=4))


scan(nmap=nmap)