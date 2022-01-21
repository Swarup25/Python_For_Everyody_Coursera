total=0
count=0
while True:
    num=input('Enter A Number: ')
    if num!='done':
        try:
            n=float(num)
        except:
            print('Invalid Input')
            continue
        total=total+n
        count=count+1
    else:
        break
print(total,count,total/count)
