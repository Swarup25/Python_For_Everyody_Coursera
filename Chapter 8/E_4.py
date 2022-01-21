t=list()
fh=open('romeo.txt')
for line in fh :
    words=line.split()
    for word in words:
        if word in t : continue
        t.append(word)
print(sorted(t))