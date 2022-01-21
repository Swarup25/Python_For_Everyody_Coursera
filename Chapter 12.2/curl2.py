import urllib.request, urllib.parse, urllib.error
img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand=open('cover2.jpg','wb')
size=0
while True:
    info=img.read(100000)
    if len(info)<1:break
    size+=len(info)
    print(len(info),size)
    fhand.write(info)
print(size,'Characters copied')
fhand.close()