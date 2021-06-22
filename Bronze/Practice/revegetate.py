fin = open('revegetate.in', 'r')
fout = open('revegetate.out', 'w')

info = fin.readline().split()
n = int(info[0])
m = int(info[1])
adjList = []*n
for i in range(n):
    adjList.append([])
seeds = [0]*n


for i in range(m):
    line = fin.readline().split()
    a = int(line[0])-1
    b = int(line[1])-1
    adjList[a].append(b)
    adjList[b].append(a)

for b in range(n):
    adjSeeds = []
    for c in range(len(adjList[b])):
        adjSeeds.append(seeds[adjList[b][c]])
    for curSeed in range(1, 5):
        seeds[b] = curSeed
        if curSeed not in adjSeeds:
            break

for c in range(n):
    fout.write(str(seeds[c]))
    
fout.close()

