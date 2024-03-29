from scapy.all import *
from bluetooth import *

def wifiPrint(pkt):
    iPhone_OUT = 'ac:07:5f'
    if pkt.haslayer(Dot11):
        wifiMAC = pkt.getlayer(Dot11).addr2
        if iPhone_OUT == wifiMAC[:8]:
            print("[*] Detected iPhone MAC: " + wifiMAC)
            btAddr = retBtAddr(wifiMAC)
            print("[+] Testing Bluetooth MAC: " + btAddr)
            checkBluetooth(btAddr)

def retBtAddr(addr):
    btAddr = str(hex(int(addr.replace(':',''), 16) + 1))[2:]
    btAddr = btAddr[0:2] + ":" + btAddr[2:4] + ":" + btAddr[4:6] + ":" + btAddr[6:8] + ":" + btAddr[8:10] + ":" + btAddr[10:12]
    return btAddr

def checkBluetooth(btAddr):
    btName = lookup_name(btAddr)
    if btName:
        print("[+] Detected Bluetooth Device: " + btName)
    else:
        print("[-] Failed to Detect Bluetooth Device")

conf.iface="wlp3s0mon"
sniff(prn=wifiPrint)