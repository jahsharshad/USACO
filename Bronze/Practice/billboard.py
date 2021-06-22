fin = open('billboard.in', 'r')
fout = open('billboard.out', 'w')

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

highy = min(y2, y4)
lowy = max(y1, y3)
lowx = max(x1, x3)
highx = min(x2, x4)

xOverlap = (x2 >= x3) and (x4 >= x1)
yOverlap = (y4 >= y2) and (y1 >= y3)
bothCorner = xOverlap and yOverlap
oneCorner = (xOverlap and not yOverlap) or (yOverlap and not xOverlap)
noCorner = not xOverlap and not yOverlap
xBetween = ((x3 <= x1) and (x1 <= x4)) and ((x3 <= x2) and (x2 <= x4))
yBetween = ((y3 <= y1) and (y1 <= y4)) and ((y3 <= y2) and (y2 <= y4))
allCorner = xBetween and yBetween

lawnmower = (x2-x1) * (y2-y1)
intersection = (highy-lowy) * (highx-lowx)
tarp = 0


if allCorner:
    tarp = 0
elif bothCorner:
    tarp = lawnmower-intersection
else:
    tarp = lawnmower


fout.write(str(tarp))
fout.close()

