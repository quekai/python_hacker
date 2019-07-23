from scapy.all import *
import sys
interface = 'wlp3s0mon'
hiddenNets = []
unhiddenNets = []

def sniffDot11(p):
    if p.haslayer(Dot11ProbeResp):
        print(p)
        addr2 = p[Dot11].addr2
        if (addr2 in hiddenNets) and (addr2 not in unhiddenNets):
            netName = p.getlayer(Dot11ProbeResp).info
            print("[+] Decloaked Hidden SSID: " + netName + " for MAC: " + addr2)
            unhiddenNets.append(addr2)
    if p.haslayer(Dot11Beacon):
        if p.getlayer(Dot11Beacon).info == '':
            addr2 = p[Dot11][Dot11Elt].addr2
            if addr2 not in hiddenNets:
                print("[-] Detected Hidden SSID: with MAC:" + addr2)
                hiddenNets.append(addr2)

sniff(iface=interface, prn=sniffDot11)

