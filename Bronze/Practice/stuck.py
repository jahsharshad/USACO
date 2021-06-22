import sys
fin = sys.stdin
fout = sys.stdout
directions = []
coordinates = []
xVals = []
yVals = []

maxx = 0
minx = 10**10

miny = 10**10
maxy = 0
n = int(fin.readline())

log = [0]*n
plane = [[True for i in range(100)] for j in range(100)]

for i in range(n):
    line = fin.readline().split()
    direct = line[0]
    directions.append(direct)
    x = int(line[1])
    y = int(line[2])
    maxx = max(maxx, x)
    minx = min(minx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)
    xVals.append(x)
    yVals.append(y)
    coord = [x, y]
    plane[x][y] = False
    coordinates.append(coord)

diffx = maxx-minx
diffy = maxy-miny
totalTime = max(diffx, diffy)



