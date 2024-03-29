import mechanize
from http import cookiejar
import random
import time

class anonBrowser(mechanize.Browser):
    def __init__(self, proxies = [], user_agents = []):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies = proxies
        self.user_agents = user_agents + ['Mozilla/5.0', 'Mozilla/4.0',]
        self.cookie_jar = cookiejar.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
        self.anonymize()

    def clear_cookies(self):
        self.cookie_jar = cookiejar.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)

    def change_user_agent(self):
        index = random.randrange(0, len(self.user_agents))
        self.addheaders = [('User-agent',(self.user_agents[index]))]

    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies({'http':self.proxies[index]})
    def anonymize(self, sleep=False):
        self.clear_cookies()
        self.change_proxy()
        self.change_user_agent()
        if sleep:
            time.sleep(60)
