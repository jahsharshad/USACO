fin = open('guess.in', 'r')
fout = open('guess.out', 'w')

length = int(fin.readline())
wholeList = []
best = 0


for i in range(length):
    line = fin.readline()
    line = line.split()
    line.pop(0)
    line.pop(0)
    wholeList.append(line)

for i in range(len(wholeList)):
    for a in range(1, len(wholeList)-i):
        animal1 = wholeList[i]
        animal2 = wholeList[i+a]
        count = 0
        for b in range(len(animal1)):
            if animal2.count(animal1[b]) == 1:
                count += 1
        best = max(best, count)

fout.write(str(best+1))
fout.close()
