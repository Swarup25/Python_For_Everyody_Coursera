def max(values):
    maximum=None
    for value in values:
        if maximum is None or value>maximum:
            maximum=value
    return maximum
values=[]
while True:
    n=input('Enter any no:')
    if n=='done':
        break
    values=str(n)
    print(values)
print('All Done')
print(max(values))
