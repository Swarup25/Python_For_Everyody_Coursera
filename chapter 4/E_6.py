def computepay(h,r):
    if h<=40:
        p=h*r
        return(p)
    else :
        p=40*r
        a=h-40
        r=r*1.5
        p2=a*r
        return(p+p2)
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
print('Pay',computepay(h,r))
