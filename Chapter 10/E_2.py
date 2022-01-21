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
    cpos=words[5].find(':')
    pword=words[5][:cpos]
    counts[pword]=counts.get(pword,0)+1
t=list(counts.items())
t.sort()
for hour,count in t:
    print(hour,count)