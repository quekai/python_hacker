import mechanize

def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    browser.set_handle_robots(None)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)

url = "http://www.baidu.com"
userAgent = [('User-agent','Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285')]
testUserAgent(url, userAgent)