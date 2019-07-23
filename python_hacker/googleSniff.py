import re
from scapy.all import *

def findGoogle(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload:
            if 'google' in payload:
                r = re.findall(r"(?i)\&q=(.*?)\&", payload)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').replace('+','').replace('%20','')
                    print("[+] Searched For: " + search)


def main():
    conf.iface = "wlp3s0mon"
    sniff(filter='tcp port 80', prn=findGoogle)

if __name__ == '__main__':
    main()