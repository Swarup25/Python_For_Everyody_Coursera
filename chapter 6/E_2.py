def count(w):
    c = 0
    for letter in w:
        if letter == 'a':
            c = c + 1
    return(c)
word=input('Please enter a word to count the letter "a":')
print('The no of letter "a" is :',count(word))
