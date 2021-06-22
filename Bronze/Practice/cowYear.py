import sys
fin = sys.stdin
fout = sys.stdout

info = fin.readline().split()
n = int(info[0])
k = int(info[1])
yrs = []
for i in range(n):
    yr = int(fin.readline())
    if yr//12 not in yrs:
        yrs.append(yr//12)

yrs.sort()

fout.write(str(len(yrs)*12))
fout.close()


    


    