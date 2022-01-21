import sqlite3
conn=sqlite3.connect('domaindb.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
fname=input("Enter the file name: ")
if len(fname) < 1:
    fname='mbox-short.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces=line.split()
    atpos=pieces[1].find('@')
    domain=pieces[1][atpos+1:]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(domain,))
    row=cur.fetchone()
    if row is None :
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''',(domain,))
    else :
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''',(domain,))
    conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()