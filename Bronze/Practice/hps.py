fin = open('hps.in', 'r')
fout = open('hps.out', 'w')

length = int(fin.readline())
cow1 = []
cow2 = []
best = 0
order = []

for i in range(length):
    line = fin.readline()
    line = line.split()
    cow1.append(int(line[0]))
    cow2.append(int(line[1]))

for i in range(6):
    wins = 0
    if i == 0:
        order = ['r', 'p', 's']
    if i == 1:
        order = ['r', 's', 'p']
    if i == 2:
        order = ['p', 'r', 's']
    if i == 3:
        order = ['p', 's', 'r']
    if i == 4:
        order = ['s', 'r', 'p']
    if i == 5:
        order = ['s', 'p', 'r']

    for b in range(len(cow1)):
        if order[int(cow1[b])-1] == 'r' and order[int(cow2[b])-1] == 's':
            wins += 1
        if order[int(cow1[b])-1] == 'p' and order[int(cow2[b])-1] == 'r':
            wins += 1
        if order[int(cow1[b])-1] == 's' and order[int(cow2[b])-1] == 'p':
            wins += 1
    best = max(best, wins)

fout.write(str(best))
fout.close()
