import sys
fin = sys.stdin
fout = sys.stdout

n = int(fin.readline())
arr = [[0 for i in range(n)] for j in range(n)]
adds = 0
coords = []

for q in range(n):
    line = fin.readline().split()
    x = int(line[0])
    y = int(line[1])
    arr[x][y] = 1
    coords.append([x, y])
    if q > 2:
        adds = 0
        for [a, b] in coords:
            if x > 0 and y > 0:
                neighbors1 = [arr[a-1][b], arr[a][b-1], arr[a+1][b], arr[a][b+1]]
                if sum(neighbors1) == 3:
                    adds += 1
        if adds > 2:
            adds += 1
    fout.write(str(adds)+'\n')


fout.close()
        
            



