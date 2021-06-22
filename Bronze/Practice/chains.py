import sys
fin = sys.stdin
fout = sys.stdout

n = int(fin.readline())

flowers = fin.readline().split()
flowers = [int(i) for i in flowers]

av = len(flowers)

for a in range(n-1):
    for b in range(n-1-a):
        sub = flowers[a:a+b+2]
        subSum = sum(sub)
        subAv = subSum/len(sub)
        if subAv in sub:
            av += 1

fout.write(str(av))
fout.close()

