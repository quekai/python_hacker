import re
from scapy.all import *
cookieTable = {}

def fireCatcher(pkt):
    raw = pkt.sprintf('%Raw.load%')
    r = re.findall('wordpress_[0-9a-fA-F]{32}', raw)
    if r and 'Set' not in raw:
        if r[0] not in cookieTable.keys():
            cookieTable[r[0]] = pkt.getlayer[IP].src
            print("[+] Detected and indexed cookie")
        elif cookieTable[r[0]] != pkt.getlayer[IP].src:
            print("[*] Detected Conflict for " + r[0])
            print("Victim = " + cookieTable[r[0]])
            print("Attacker = " + pkt.getlayer(IP).src)
        

conf.iface = 'wlp3s0mon'
sniff(filter="tcp port 80", prn=fireCatcher)