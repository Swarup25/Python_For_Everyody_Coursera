import re
inp=input("Please enter the file name:")
file=open(inp)
nlist=[]
for line in file:
    line.rstrip()
    stuff=re.findall('^New Revision: ([0-9.]+)',line)
    if len(stuff)==0:continue
    intstuff=int(stuff[0])
    nlist.append(intstuff)
print(int(sum(nlist)/len(nlist)))
