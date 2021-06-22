fin = open('shell.in', 'r')
fout = open('shell.out', 'w')

length = int(fin.readline())
order = [1, 2, 3]
guessList = []

for i in range(length):
    line = fin.readline()
    line = line.split()
    swap1 = int(line[0])
    swap2 = int(line[1])
    order[swap1-1], order[swap2-1] = order[swap2-1], order[swap1-1]
    guess = int(line[2])
    guessList.append(order[guess-1])

count = -100
for i in range(len(guessList)):
    tempCount = guessList.count(guessList[i])
    count = max(count, tempCount)

fout.write(str(count))
fout.close()    
