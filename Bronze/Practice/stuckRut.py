import sys
fin = sys.stdin
fout = sys.stdout

directions = []
coordinates = []
north = []
east = []
who = []
when = []
log = []

n = int(fin.readline())

for i in range(n):
    line = fin.readline().split()
    direct = line[0]
    directions.append(direct)
    x = int(line[1])
    y = int(line[2])
    coord = [x, y]
    coordinates.append(coord)
    if direct == 'N':
        north.append(coord)
    elif direct == 'E':
        east.append(coord)

north.sort()
east.sort(key=lambda q: (q[1]))

for a in range(n):
    grass = 10**10
    state = directions[a]
    position1 = coordinates[a]
    x1 = position1[0]
    y1 = position1[1]
    time = 0
    stopper = 0
    if state == 'N':
        for b in range(len(east)):
            position2 = east[b]
            x2 = position2[0]
            y2 = position2[1]
            width = x1-x2
            height = y2-y1
            if height > 0 and width > 0:
                if width < height:
                    grass = min(grass, height)
                    if grass == height:
                        time = height
                        stopper = coordinates.index(position2)+1
        who.append(stopper)
    elif state == 'E':
        for c in range(len(north)):
            position3 = north[c]
            x3 = position3[0]
            y3 = position3[1]
            width = x3-x1
            height = y1-y3
            if width > 0 and height > 0:
                if height < width:
                    grass = min(grass, width)
                    if grass == width:
                        time = width
                        stopper = coordinates.index(position3)+1

        who.append(stopper)
    when.append(time)
    log.append(grass)

for x in range(n):
    member = who[x]
    hour1 = when[x]
    hour2 = when[member-1]
    if (hour1 > hour2) and hour2:
        who[x] = 0
        when[x] = 0
        log[x] = 10**10


for d in range(len(log)):
    if log[d] == 10**10:
        fout.write('Infinity')
    else:
        fout.write(str(log[d]))
    if d != (len(log)-1):
        fout.write('\n')

fout.close()
