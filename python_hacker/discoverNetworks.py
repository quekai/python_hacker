from winreg import *
import mechanize, urllib, re
from urllib.parse import urlparse
import os
import optparse

def wiglePrint(username, password, netid):
    browser = mechanize.Browser()
    browser.open("http://wigle.net")
    reqData = urllib.parse.urlencode({'credential_0': username, 'credential_1': password})
    browser.open("https://wigle.net/gps/gps/main/login", reqData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.parse.urlencode(params)
    respURL = "http://wigle.net/gps/gps/main/confirmquery/"
    resp = browser.open(respURL, reqParams).read()
    mapLat = 'N/A'
    mapLon = 'N/A'
    rLat = re.findall(r'maplat=.*\&', resp)
    if rLat:
        mapLat = rLat[0].split('&')[0].split('=')[1]
    rLon = re.findall(r'maplon=.*\&', resp)
    if rLon:
        mapLon = rLon[0].split('&')[0].split('=')[1]
    print("[-] Lat: " + mapLat + ", Lon: " + mapLon)

def printNets(username, password):
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print("\n[*] Networks you have joined")
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print("[+] " + netName + " " + macAddr)
            wiglePrint(username, password, macAddr)
            CloseKey(netKey)
        except:
            break

def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x "% ch)
    addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr

def main():
    parser = optparse.OptionParser("usage%prog " + "-u <wigle username> -p <wigle password>")
    parser.add_option('-u', dest='username', type='string', help='specify wigle username')
    parser.add_option('-p', dest='password', type='string', help='specify wigle password')
    (options, args) = parser.parse_args()
    username = options.username
    password = options.password
    if username is None or password is None:
        print(parser.usage)
        exit(0)
    else:
        printNets(username, password)

if __name__ == '__main__':
    main()