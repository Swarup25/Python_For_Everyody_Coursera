import socket
url=input('Please enter the URL:')
try:
    pos=url.split('/')
    host=pos[2]
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect((host,80))
except:
    print('You entered an improperly formatted or non-existent URL!!')
    exit()
cmd=('GET '+url+' HTTP/1.0\r\n\r\n').encode()
mysocket.send(cmd)
while True:
    data=mysocket.recv(5120)
    if len(data)<1:break
    print(data.decode(),end='')
mysocket.close()
