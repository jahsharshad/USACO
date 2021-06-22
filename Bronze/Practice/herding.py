fin = open('herding.in', 'r')
fout = open('herding.out', 'w')

bestMin = 0
bestMax = 0
places = fin.readline().split()
places = [int(i) for i in places]
places.sort()
a = places[0]
b = places[1]
c = places[2]

if c == (a+2):
    bestMin = 0
elif (b == a+2) or (c == b+2):
    bestMin = 1
else:
    bestMin = 2

bestMax = max(b - a, c - b)
bestMax -= 1

fout.write(str(bestMin)+'\n')
fout.write(str(bestMax))
fout.close()
