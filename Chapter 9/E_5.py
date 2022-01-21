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
    atpos=words[1].find('@')
    pword=words[1][atpos+1:]
    count[pword]=count.get(pword,0)+1
print(count)