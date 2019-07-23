import dpkt
import socket
import geoip2.database
import optparse
gi = geoip2.database.Reader('GeoLite2-City/GeoLite2-City.mmdb')

def retGeoStr(ip):
    try:
        rec = gi.city(ip)
        city = rec.city.name
        country = rec.country.name
        if city != '':
            geoLoc = city + ", " + country
        else:
            geoLoc = country
        return geoLoc
    except:
        return "Unregistered"



def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print("[+] Src: " + src + " --> Dst: " + dst)
            print("[+] Src: " + retGeoStr(src) + " --> Dst: " + retGeoStr(dst))
        except:
            pass

def main():
    parser = optparse.OptionParser("usage%prog -p <pcap file>")
    parser.add_option('-p', dest='pcapFile', type='string', help='specify pcap filename')
    (options, args) = parser.parse_args()
    if options.pcapFile is None:
        print(parser.usage)
        exit(0)
    pcapFile = options.pcapFile
    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

if __name__ == '__main__':
    main()