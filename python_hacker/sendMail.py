import smtplib
from email.mime.text import MIMEText

def sendMail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP_SSL('smtp.qq.com', 465)
        print("[+] Connecting To Mail Server.")
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except:
        print("[-] Sending Mail Failed.")

user = '***@qq.com'
pwd = '***'
sendMail(user,pwd,'***@qq.com','Re:important','Test Message.')