fin = open('shuffle.in', 'r')
fout = open('shuffle.out', 'w')

length = int(fin.readline())
pos1 = [1, 2, 3, 4, 5]
outList = []
for i in range(length):
    outList.append(0)

line1 = fin.readline()
pos = line1.split()

line2 = fin.readline()
ID = line2.split()
temp = ID

for i in range(3):
    temp = []
    for c in range(length):
        temp.append(0)
    for b in range(length):
        temp[b] = ID[int(pos[b])-1]
    ID = temp

for i in range(len(ID)):
    fout.write(str(ID[i])+'\n')

fout.close()


