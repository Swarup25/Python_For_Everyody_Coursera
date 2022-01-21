count=0
fh=open('mbox-short.txt')
for line in fh :
    if not line.startswith('From ') : continue
    words=line.split()
    if len(words) < 3 : continue
    print (words[1]) 
    count=count+1
print("There were", count, "lines in the file with From as the first word")