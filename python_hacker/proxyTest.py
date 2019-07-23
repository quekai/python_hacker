import mechanize

def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    browser.set_handle_robots(None)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)

url = "http://www.baidu.com"
hideMeProxy = {'http':'101.37.20.241:443'}
testProxy(url, hideMeProxy)