import string
counts=dict()
fh=input("Please enter the file name:")
#try:
file=open(fh)
#except:
 #   print("Please enter a valid file name!")
    #exit()
for line in file: 
    line.rstrip()
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.translate(str.maketrans('','',string.digits))
    line=line.lower()
    words=line.split()
    for word in words:
        for letter in word:
            counts[letter]=counts.get(letter,0)+1
t=list()
for word,count in list(counts.items()):
    t.append((count,word))
t.sort(reverse=True)
for count,word in t:
    print(word,count)