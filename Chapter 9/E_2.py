count=dict()
fh=input('Enter the mail box text:')
try:
    file=open(fh)
except:
    print("Please enter valid file name!")
    exit()
for line in file:
    line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    count[words[2]]=count.get(words[2],0)+1
print(count)

