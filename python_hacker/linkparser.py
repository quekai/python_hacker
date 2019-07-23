from anonBrowser import *
from bs4 import BeautifulSoup
import os
import re

def printLinks(url):
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(url)
    html = page.read()
    try:
        print("[+] Printing Links From Regex.")
        link_finder = re.compile('href="(.*?)"')
        links = link_finder.findall(html)
        for link in links:
            print(link)
    except:
        pass
    try:
        print("[+] Printing Links From BeautifulSoup")
        soup = BeautifulSoup(html)
        links = soup.findAll(name='a')
        for link in links:
            if link.has_attr('href'):
                print(link['href'])
    except:
        pass
def main():
    url = "http://www.baidu.com"
    printLinks(url)

if __name__ == '__main__':
    main()