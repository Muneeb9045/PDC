import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

serversocket.bind((host, port))
serversocket.Listen(5)

while True:
    clientsocket.addr = serversocket.accept()
    print("Connected with[addr],[port]%s"%str(addr))
    currentTime = time.ctime(time.time())+"\rvn"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()