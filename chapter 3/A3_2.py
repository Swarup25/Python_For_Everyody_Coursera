score=input("Enter a score between 0.0 to 1.0 :")
s=float(score)
if s<=1.0 and s>=0.9:
    print('A')
elif s<=1.0 and s>=0.8:
    print('B')
elif s<=1.0 and s>=0.7:
    print('C')
elif s<=1.0 and s>=0.6:
    print('D')
elif s<=1.0 and s<0.6:
    print('F')
elif s>1.0:
    print('Bad score')
    quit()
elif s<0.0:
    print('Bad score')
    quit()
