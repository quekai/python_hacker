from bluetooth import *
import time
alreadyFound = []

def findDevs():
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in alreadyFound:
            print("[+] Found BLuetooth Device " + str(name))
            print("[+] Mac address: " + str(addr))
            alreadyFound.append(addr)

while True:
    findDevs()
    time.sleep(5)