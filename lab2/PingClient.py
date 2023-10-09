# Python3


from socket import *
import sys
import time
import statistics
import random

def ping (host,port):
    serverName = host
    serverPort = port
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    seqNum = random.randint(10000,20000)
    pingSum = 0
    rtt = []
    while(pingSum < 20):
        pingSum += 1
        startTime = time.time() * 1000
        message = 'PING' + ' ' + str(seqNum) + ' ' + str(startTime) + '\r\n'
        clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))
        clientSocket.settimeout(0.6)
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            getTime = time.time() * 1000
            useTime = getTime - startTime
            rtt.append(useTime)
            print(f'ping to {serverName}, seq = {seqNum}, rtt = {int(useTime)} ms')
            seqNum += 1
        except timeout:
            print(f'ping to {serverName}, seq = {seqNum}, time out')
            seqNum += 1
    print('20 pings done')
    if len(rtt) > 0:
        minrtt = min(rtt)
        maxrtt = max(rtt)
        avertt = statistics.mean(rtt)
        print(f'MINIMUM RTT = {int(minrtt)} ms, MAXIMUM RTT = {int(maxrtt)} ms, AVERAGE RTT = {int(avertt)} ms\n')
    else:
        print('ALL TIME OUT,Check Host port again\n')
    clientSocket.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('required host port')
        exit(1)
    host = sys.argv[1]
    port = int (sys.argv[2])
    ping(host, port)