from socket import *
import sys

def start (port, noFails):
    serverPort = port
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Creates the TCP servers socket.
    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(5)
    print("The server is ready to receive!")
    print(f"The server is running on http://127.0.0.1:{serverPort}/index.html")
    while 1:
        connectionSocket, addr = serverSocket.accept()
        response(connectionSocket)

def response(connectionSocket):
    sentence = connectionSocket.recv(1024)
    filename = sentence.split()
    try:
        data = open(filename[1][1:],'rb').read()
        print(f'request {filename[1][1:]} \n')
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n')
        if 'png' in str(filename[1][1:]):
            connectionSocket.send(b'Content-Type: image/png \r\n\r\n')
        else:
            connectionSocket.send(b'Content-Type: text/html \r\n\r\n')
        connectionSocket.send(data)
        connectionSocket.close()
    except IOError:
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n')
        connectionSocket.send(b'Content-Type: text/html \r\n\r\n')
        connectionSocket.send(b'<html><h1>404 File Not Found try index.html or myimage.png</h1></html>')
        connectionSocket.close()

if __name__ == '__main__':
    if len(sys.argv) < 1 or len(sys.argv) > 3:
        print('required port and no. of failed attempts or error input')
        exit(1)
    port = int (sys.argv[1])
    noFails = int (sys.argv[2])
    if port == 80 or port == 8080 or port < 1024:
        print('use a non-standard port no.')
        exit(1)
    if noFails <= 1 or noFails >= 5:
        print('invalid number')
        exit(1)
    start(port, noFails)