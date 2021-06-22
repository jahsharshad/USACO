import math
fin = open('traffic.in', 'r')
fout = open('traffic.out', 'w')

length = int(fin.readline())
state = []
lower = []
upper = []

for i in range(length):
    line = fin.readline()
    line = line.split()
    state.append(line[0])
    lower.append(int(line[1]))
    upper.append(int(line[2]))

a = -math.inf
b = math.inf

for i in range(length-1, -1, -1):
    if state[i] == 'none':
        a = max(a, lower[i])
        b = min(b, upper[i])
    if state[i] == 'off':
        a += lower[i]
        b += upper[i]
    if state[i] == 'on':
        a -= upper[i]
        b -= lower[i]
        a = max(0, a)
        
fout.write(str(a)+' '+str(b)+'\n')

a = -math.inf
b = math.inf

for i in range(length):
    if state[i] == 'none':
        a = max(a, lower[i])
        b = min(b, upper[i])
    if state[i] == 'on':
        a += lower[i]
        b += upper [i]
    if state[i] == 'off':
        a -= upper[i]
        b -= lower[i]
        a = max(0, a)

fout.write(str(a)+' '+str(b))
fout.close()

