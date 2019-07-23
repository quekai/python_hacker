from scapy.all import *
from IPy import IP as IPTEST

ttlValues = {}
THRESH = 5

def checkTTL(ipsrc, ttl):
    if IPTEST(ipsrc).iptype() == "PRIVATE":
        return
    if not ttlValues.__contains__(ipsrc):
        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry=0, timeout=1, verbose=0)
        ttlValues[ipsrc] = pkt.ttl
    if abs(int(ttl) - int(ttlValues[ipsrc])) > THRESH:
        print("\n[!] Detected Possible Spoofed Packet From: " + ipsrc)
        print("[!] TTL: " + ttl + ", Actual TTL: " + str(ttlValues[ipsrc]))

def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            checkTTL(ipsrc, ttl)
    except:
        pass

def main():
    sniff(prn=testTTL, store=0)

if __name__ == '__main__':
    main()