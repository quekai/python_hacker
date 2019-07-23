from scapy.all import *

def calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1,5):
        if preNum != 0:
            preNum = seqNum
        ans = srl(IP(dst=tgt) / TCP(), retry=0, timeout=1, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print("[+] TCP Seq difference: " + str(diffSeq))
    return seqNum + diffSeq

tgt = "192.168.1.106"
seqNum = calTSN(tgt)
print("[+] Next TCP Sequence Number to ACK is: " + str(seqNum+1))