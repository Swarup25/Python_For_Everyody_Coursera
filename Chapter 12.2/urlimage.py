import socket
import time
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
mysock.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\r\n\r\n')
count=0
picture=b''
while True:
    data=mysock.recv(5120)
    if len(data)<1:break 
    time.sleep(0.25)#delay
    count+=len(data)
    print(len(data),count)
    picture+=data
mysock.close()
# Look for the end of the header (2 CRLF)
pos=picture.find(b'\r\n\r\n')
print('Header length :',pos)
print(picture[:pos].decode())
# Skip past the header and save the picture data
picture=picture[pos+4:]
fhand=open('cover.jpg','wb')
fhand.write(picture)
fhand.close()