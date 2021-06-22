fin = open('breedflip.in', 'r')
fout = open('breedflip.out', 'w')

n = int(fin.readline())
times = 0

group1 = list(fin.readline())
group2 = list(fin.readline())
cows = []

for i in range(n):
    if group1[i] == group2[i]:
        cows.append(True)
    else:
        cows.append(False)

charge = cows[0]
for b in range(n):
    status = cows[b]
    if status:
        charge = True
    if not status:
        if charge:
            times += 1
            charge = False
        else:
            if b == 0:
                times += 1
            charge = False

fout.write(str(times))
fout.close()
