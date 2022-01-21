nd=dict()
file=open('words.txt')
for line in file :
    words=line.split()
    for word in words :
        nd[word]=nd.get('word',0)+1
print(nd)