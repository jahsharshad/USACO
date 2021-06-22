fin = open('circlesum.in', 'r')
fout = open('circlesum.out', 'w')

numofnum = int(fin.readline())
intlist = []
for i in range(numofnum):
    intlist.append(fin.readline())

intlist = [int(i) for i in intlist]
sumlist = sum(intlist)
certainsum = 0
for i in range(len(intlist)):
    intlist.insert(0, intlist[len(intlist)-1])
    intlist.pop()
    for y in range(len(intlist)):
        for x in range(y, len(intlist)):
            if certainsum > sumlist:
                sumlist = certainsum
            certainsum = 0
            for b in range(y, x+1):
                certainsum += intlist[b]

fout.write(str(sumlist))
fout.close()



