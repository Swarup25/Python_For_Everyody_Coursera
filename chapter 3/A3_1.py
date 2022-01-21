hrs=input('Enter the Hour:')
try:
    h=float(hrs)
except:
    print("Please enter numeric input")
    quit()
rate=input("Enter the Rate per hour:")
try:
    r=float(rate)
except:
    print("Please enter numeric input")
    quit()
if h<=40:
    p=h*r
    print(p)
else :
    p=40*r
    a=h-40
    r=r*1.5
    p2=a*r
    print(p+p2)
