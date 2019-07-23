import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS
import optparse


def findImages(url):
    print("[+] Finding images on " + url)
    urlContent = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent, 'lxml')
    imgTags = soup.findAll('img')
    return imgTags


def downloadImage(url, imgTag):
    try:
        print("[+] Downloading image...")
        imgSrc = imgTag['src']
        imgSrc = url + imgSrc
        print(imgSrc)
        imgContent = urllib.request.urlopen(imgSrc).read()
        imgFileName = basename(urllib.parse.urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''


def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            exifModel = exifData['Model']
            exifDate = exifData['DateTimeDigitized']
            exifArtist = exifData['Artist']
            if exifGPS:
                print("[*] " + imgFileName + " contains GPS MetaData")
            if exifModel:
                print("[*] " + imgFileName + " contains Make: " + exifModel)
            if exifDate:
                print("[*] " + imgFileName + " contains Date: " + exifDate)
            if exifArtist:
                print("[*] " + imgFileName + " contains Artist: " + exifArtist)
    except:
        pass


def main():
    parser = optparse.OptionParser("usage %prog " + "-u <target url>")
    parser.add_option('-u', dest='url', type='string', help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url
    if url is None:
        print(parser.usage)
        exit(0)
    else:
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(url, imgTag)
            testForExif(imgFileName)



if __name__ == '__main__':
    main()
