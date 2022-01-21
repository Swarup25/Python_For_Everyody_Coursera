counts=dict()
fh=input("Enter the file name:")
try:
    file=open(fh)
except:
    print("Please enetr a valid file name")
    exit()
for line in file:
    line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    counts[words[1]]=counts.get(words[1],0)+1
t=list()
for email,count in list(counts.items()):
    t.append((count,email))
t.sort(reverse=True)
for count,email in t[:1]:
    print(email,count)


