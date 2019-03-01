'''Code below is used to establish a connection with a Webserver.. 
We are not sending data.. like dailing the phone to the Webserver
Last Line: mysock.connect(('Host we are wanting to connect to', Port 80))'''

import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/clown.txt HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)


'''While loop and receive method essentially is allowing our 
connection to request 512 characters at a time until the 
server doesnt have anything else to send 
and then break our connection.'''
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()