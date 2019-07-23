import obexftp
try:
    btPrinter = obexftp.client(obexftp.BLUETOOTH)
    btPrinter.connect("AC:07:5F:6B:1F:11", 9)
    btPrinter.put_file('a20190608162223.png')
    print("[+] Printed Image.")
except:
    print("[-] Failed to print Image.")