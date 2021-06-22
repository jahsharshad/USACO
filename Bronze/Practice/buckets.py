fin = open('buckets.in', 'r')
fout = open('buckets.out', 'w')

for a in range(10):
    line = fin.readline()
    for b in range(10):
        if line[b] == 'B':
            barnRow = a
            barnCol = b
        elif line[b] == 'R':
            rockRow = a
            rockCol = b
        elif line[b] == 'L':
            lakeRow = a
            lakeCol = b

bl = abs(barnRow-lakeRow)+abs(barnCol-lakeCol)
br = abs(barnRow-rockRow)+abs(barnCol-rockCol)
rl = abs(rockRow-lakeRow)+abs(rockCol-lakeCol)

if (barnCol == lakeCol or barnRow == lakeRow) and (bl == br + rl):
    ans = bl + 1
else:
    ans = bl - 1

fout.write(str(ans))
fout.close()
