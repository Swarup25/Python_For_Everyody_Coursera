#Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.

def chop(t):
    del t[0]
    del t[-1]
def middle(t):
    return t[1:-1]
print('________Please crate a list________')
nlist=list()
while (True) :
    value=input('Please enter the element to be inserted :')
    if value == 'done' : break
    nlist.append(value)
while True :
    option=input('Please tell which operaton to do--chop or middle:')
    if option == "chop":
        a=chop(nlist)
        print('The list after chopping is:',nlist)
        break
    elif option == "middle" :
        print('The new list after middling is:',middle(nlist))
        break
    else:
        print("Please tell your choice correctly")
        continue
