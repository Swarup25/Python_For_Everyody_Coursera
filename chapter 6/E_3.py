str = 'X-DSPAM-Confidence:0.8475'
a=str.find('0')
b=str[a:]
c= float(b)
print(c)
