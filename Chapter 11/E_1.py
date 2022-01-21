import re
c=0
in_ex=input("Please enter a expresion:")
reg_ex=str(in_ex)
filen='mbox.txt'
file=open(filen)
for line in file:
    line.rstrip()
    if re.findall(reg_ex,line) !=[]:
        c+=1
print(filen , 'had',c,'lines that matched', reg_ex)