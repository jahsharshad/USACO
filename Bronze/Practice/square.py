fin = open('square.in', 'r')
fout = open('square.out', 'w')

coordinateList = []
for i in range(2):
    coordinateList.append(fin.readline())

for i in range(len(coordinateList)):
    coordinateList[i] = coordinateList[i].split()
    coordinateList[i] = [int(x) for x in coordinateList[i]]

x1 = int(coordinateList[0][0])
y1 = int(coordinateList[0][1])
x2 = int(coordinateList[0][2])
y2 = int(coordinateList[0][3])

x3 = int(coordinateList[1][0])
y3 = int(coordinateList[1][1])
x4 = int(coordinateList[1][2])
y4 = int(coordinateList[1][3])

highy = max(y2, y4)
lowy = min(y1, y3)
lowx = min(x1, x3)
highx = max(x2, x4)

xlength = highx-lowx
ylength = highy-lowy
length = max(xlength, ylength)
area = length**2


fout.write(str(area))
fout.close()