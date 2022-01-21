import socket
url=input('Please ENter the URL:')
try:
    host=url.split('/')[2]
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host,80))
except:
    Print('The URL is improperly formatted or non-existent')
    exit()
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())
received=b""
while True:
    data=mysock.recv(512)
    if len(data)<1:break 
    received+=data
received=received.decode()
pos=received.find('\r\n\r\n')
content=received[pos+4:]
print(content.strip())
