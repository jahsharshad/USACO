fin = open('reverseprint.in', 'r')
fout = open('reverseprint.out', 'w')

numofnum = int(fin.readline())
intlist = []
for i in range(numofnum):
    intlist.insert(0, fin.readline())

for i in range(0, len(intlist)):
    fout.write(intlist[i])
fout.close()
