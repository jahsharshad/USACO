import sys
fin = sys.stdin
fout = sys.stdout

directions = []
coordinates = []
north = []
east = []


lineNum = int(fin.readline())
times = [0]*lineNum
stopped = [False]*lineNum

for i in range(lineNum):
    line = fin.readline().split()
    dir = line[0]
    directions.append(dir)
    x = line[1]
    y = line[2]
    coord = [x, y]
    coordinates.append(coord)
    if dir == 'N':
        north.append(coord)
    elif dir == 'E':
        east.append(coord)

for i in range(len(directions)):
    state = directions[i]
    x1 = coordinates[i][0]
    y1 = coordinates[i][1]
    least = 10**10
    if state == 'N':
        for a in range(len(east)):
            x2 = north[a][0]
            y2 = north[a][1]
            width = x1-x2
            height = y2-y1
            if (width > 0 and height > 0) and width < height:
                least = min(least, height)
    elif state == 'E':
        for b in range(len(north)):
            x3 = north[b][0]
            y3 = north[b][1]
            width = x3-x1
            height = y1-y3
            if (width > 0 and height > 0) and width < height:
                least = min(least, height)





            

