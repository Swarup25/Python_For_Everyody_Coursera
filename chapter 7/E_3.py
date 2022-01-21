fname=input('Eter te file name:')
count=0
try:
    fh=open(fname)
    for line in fh :
        count=count+1
    print('There were', count, 'subject lines in', fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - you have been punk'd!")
    else :
        print('File cannot be opened:',fname)
