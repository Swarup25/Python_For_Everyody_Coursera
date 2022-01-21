import re
numlist=[]
file=open('actual.txt')  # I renamed the file as actual.txt
for line in file :
    line.rstrip()
    stuff=re.findall('[0-9]+',line)
    if len(stuff)==0:continue
    for i in range(len(stuff)):
        intstuff=int(stuff[i])
        numlist.append(intstuff)
        i+=1
print(sum(numlist))