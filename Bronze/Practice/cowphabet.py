import sys
fin = sys.stdin
fout = sys.stdout

# fin = open('1.in', 'r')
# fout = open('bet.out', 'w')


alpha = fin.readline()
heard = fin.readline()
times = 0

for i in range(len(heard)-1):
    if alpha.index(heard[i]) >= alpha.index(heard[i+1]):
        times += 1

fout.write(str(times+1))
fout.close()


