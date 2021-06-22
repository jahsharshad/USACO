import sys
fin = sys.stdin
fout = sys.stdout

# fin = open('1.in', 'r')
# fout = open('stall.out', 'w')


length = int(fin.readline())
heights = fin.readline().split()
limits = fin.readline().split()

heights = [int(i) for i in heights]
limits = [int(i) for i in limits]

heights.sort()
limits.sort()
heights.reverse()
limits.reverse()

times = []

for a in range(len(heights)):
    height = heights[a]
    poss = 0
    for b in limits:
        limit = b
        if height > limit:
            break
        else:
            poss += 1
    times.append(poss-a)

ways = 1

for c in times:
    ways *= c

fout.write(str(ways))
fout.close()
