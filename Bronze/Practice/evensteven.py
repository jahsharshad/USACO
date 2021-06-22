fin = open('evensteven.in', 'r')
fout = open('evensteven.out', 'w')

fin = fin.read()
maxnum = int(fin)

for i in range(1, maxnum+1):
    if i % 2 == 0:
        fout.write(str(i))
        fout.write('\n')
fout.close()
