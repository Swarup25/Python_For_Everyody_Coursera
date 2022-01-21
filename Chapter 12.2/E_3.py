import urllib.request,urllib.parse, urllib.error
count=0
url=input("please emter the URL:")
fhand=urllib.request.urlopen(url)
for line in fhand:
    line=line.decode()
    count+=len(line)
    if count <= 3000 :
        print(line.rstrip())
    

print("No of characters received:",count)
