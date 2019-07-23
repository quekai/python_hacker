from anonBrowser import *
from bs4 import BeautifulSoup
import os

def mirrorImages(url, dir):
    ab = anonBrowser()
    ab.anonymize()
    html = ab.open(url)
    soup = BeautifulSoup(html)
    image_tags = soup.findAll('img')
    for image in image_tags:
        filename = image['src'].lstrip('http://')
        filename = os.path.join(dir, filename.replace('/', '_'))
        print("[+] Saving " + str(filename))
        data = ab.open(image['src']).read()
        ab.back()
        save = open(filename, 'wb')
        save.write(data)
        save.close()
def main():
    url = "http://xkcd.com"
    dir="/tmp/"
    mirrorImages(url, dir)

if __name__ == '__main__':
    main()