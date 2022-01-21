def computegrade(s):
    if s<=1.0 and s>=0.9:
        return('A')
    elif s<=1.0 and s>=0.8:
        return('B')
    elif s<=1.0 and s>=0.7:
        return('C')
    elif s<=1.0 and s>=0.6:
        return('D')
    elif s<=1.0 and s<0.6:
        return('F')
    elif s>1.0:
        return('Bad score')
        quit()
    elif s<0.0:
        return('Bad score')
        quit()
score=input("Enter a score between 0.0 to 1.0 :")
try:
    s=float(score)
except:
    print('Bad Score')
    quit()
print(computegrade(s))   
