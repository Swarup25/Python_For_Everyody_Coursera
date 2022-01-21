fname=input("Enter the file name:")
fh=open(fname)
for lx in fh :
    ly=lx.rstrip()
    print(ly.upper())
