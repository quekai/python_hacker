from scapy.all import *

def pktPrint(pkt):
    if pkt.haslayer(Dot11Beacon):
        print("[+] Detected 802.11 Beacon Frame")
    elif pkt.haslayer(Dot11ProbeReq):
        print("[+] Detected 802.11 Probe Request Frame")
    elif pkt.haslayer(TCP):
        print("[+] Detected a TCP packet")
    elif pkt.haslayer(DNS):
        print("[+] Detected a DNS packet")


sniff(prn=pktPrint,iface='wlp3s0mon')