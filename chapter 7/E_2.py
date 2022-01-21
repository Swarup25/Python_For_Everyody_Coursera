fname=input('Enter the file name:')
fh=open(fname)
c=0
t=0
for line in fh :
    if line.startswith('X-DSPAM-Confidence:') :
        c=c+1
        pos=line.find(':')
        nl=line[pos+1:]
        a=float(nl)
        t=t+a
    else :
        continue
print('Average spam confidence:',t/c)
