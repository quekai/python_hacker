import geoip2.database

gi = geoip2.database.Reader('GeoLite2-City/GeoLite2-City.mmdb')

def printRecord(tgt):
    rec = gi.city(tgt)
    city = rec.city.name
    country = rec.country.name
    long = rec.location.longitude
    lat = rec.location.latitude
    print("[*] Target: " + tgt + ' Geo-located')
    print("[+] " + str(city) + ", " + str(country))
    print("[+] Latitude: " + str(lat) + ", Longitude: " + str(long))

tgt = "47.107.152.110"

printRecord(tgt)
