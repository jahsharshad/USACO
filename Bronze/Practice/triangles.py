fin = open('triangles.in', 'r')
fout = open('triangles.out', 'w')

points = []
area = 0
n = int(fin.readline())

for i in range(n):
    point = fin.readline().split()
    point = [int(i) for i in point]
    points.append(point)

length = len(points)

for a in range(length-2):
    vertice1 = points[a]
    x1 = vertice1[0]
    y1 = vertice1[1]

    for b in range(a+1, length-1):
        vertice2 = points[b]
        x2 = vertice2[0]
        y2 = vertice2[1]

        for c in range(b+1, length):
            vertice3 = points[c]
            x3 = vertice3[0]
            y3 = vertice3[1]

            xAllowed = False
            yAllowed = False
            height = 0
            width = 0

            if x1 == x2:
                xAllowed = True
                height = abs(y1-y2)
            if x2 == x3:
                xAllowed = True
                height = abs(y2 - y3)
            if x1 == x3:
                xAllowed = True
                height = abs(y1 - y3)

            if y1 == y2:
                yAllowed = True
                width = abs(x1 - x2)
            if y2 == y3:
                yAllowed = True
                width = abs(x2 - x3)
            if y1 == y3:
                yAllowed = True
                width = abs(x1 - x3)

            if yAllowed and xAllowed:
                currentArea = height*width
                area = max(area, currentArea)
fout.write(str(area))
fout.close()
