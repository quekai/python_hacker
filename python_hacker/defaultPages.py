import ftplib

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for filename in dirList:
        fn = filename.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + filename)
            retList.append(filename)
    return  retList

host = '192.168.95.179'
userName = 'guest'
password = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName, password)
returnDefault(ftp)