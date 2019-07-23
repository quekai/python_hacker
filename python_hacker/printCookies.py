import mechanize
from http import cookiejar

def printCookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookiejar.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    for cookie in cookie_jar:
        print(cookie)

url = "http://www.syngress.com"
printCookies(url)