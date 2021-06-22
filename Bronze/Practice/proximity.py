fin = open('proximity.in', 'r')
fout = open('proximity.out', 'w')

firstLine = fin.readline().split()
n = int(firstLine[0])
k = int(firstLine[1])
idList = []
account = [0] * 1000000
maxBreed = -1


for i in range(n):
    idList.append(int(fin.readline()))

for i in range(n-k):
    if i == 0:
        for b in range(k+1):
            account[idList[i+b]] += 1
            if (account[idList[i+b]] > 1) and (idList[i+b] > maxBreed):
                maxBreed = idList[i+b]
    else:
        account[idList[i-1]] -= 1
        account[idList[i+k]] += 1
        if (account[idList[i+k]] > 1) and (idList[i+k] > maxBreed):
            maxBreed = idList[i+k]
fout.write(str(maxBreed))
fout.close()
