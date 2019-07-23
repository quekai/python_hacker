from scapy.all import *
import re

def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = pkt.findall('(?i)USER (.*)', raw)
    pswd = pkt.findall('(?i)PASS (.*)', raw)
    if user:
        print("[*] Detected FTP Login to " + str(dest))
        print("[+] User account: " + str(user[0]))
    elif pswd:
        print("[+] Password: " + str(pswd[0]))

def main():
    conf.iface = "wlp3s0mon"
    sniff(filter='tcp port 21', prn=ftpSniff)

if __name__ == '__main__':
    main()