fin = open('copymachine.in', 'r')
fout = open('copymachine.out', 'w')

numofnum = int(fin.readline())
intlist = []
for i in range(numofnum):
    intlist.append(fin.readline())

for i in range(0, len(intlist)):
    fout.write(intlist[i])

fout.close()
