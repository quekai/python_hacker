from anonBrowser import *

ab = anonBrowser(proxies=[], user_agents=[('User-agent','Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285')])

for attempt in range(1,5):
    ab.anonymize()
    print('[*] Fetching page')
    response = ab.open('http://kittenwar.com')
    for cookie in ab.cookie_jar:
        print(cookie)