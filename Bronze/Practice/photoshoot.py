fin = open('photo.in', 'r')
fout = open('photo.out', 'w')

n = int(fin.readline())
permB = fin.readline().split()
permB = [int(i) for i in permB]

permA = []
start = 1
if permB[0] > n:
    start = permB[0] - n

for i in range(start, permB[0]):
    current = [i]
    if i < (len(current)-1):
        fout.write(' ')
    for b in range(n-1):
        new = permB[b]-current[len(current)-1]
        if (new in current) or (new < 1):
            current = []
            break
        else:
            current.append(new)
    if len(current) == n:
        break

for i in range(len(current)):
    fout.write(str(current[i]))


fout.close()
