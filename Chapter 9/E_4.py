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
    count[words[1]]=count.get(words[1],0)+1
mostm=None
nom=None
for key,value in count.items():
    if nom is None or value>nom :
        mostm=key
        nom=value
print (mostm,nom)