import socket
import time
url=input('Please Enter a URL:')
count=b""
try:
    host=url.split('/')[2]
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host,80))
except:
    print('You entered an improperly formatted or non-existent URL!!')
    exit()
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())

while True:
    data=mysock.recv(512)
    if len(data)<1:break 
    time.sleep(0.25)
    count+=data
characters=count.decode()
print(characters[:3000])
print('No of characters is:',len(characters))