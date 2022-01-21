import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
filehand=open('stuff.jpg','wb')
filehand.write(fhand)
filehand.close()