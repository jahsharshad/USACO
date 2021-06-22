fin = open('blist.in', 'r')
fout = open('blist.out', 'w')


n = int(fin.readline())
buckets = [0]*1001

for i in range(n):
    line = fin.readline().split()
    start = int(line[0])
    end = int(line[1])
    num = int(line[2])
    for b in range(start, end+1):
        buckets[b] += num

fout.write(str(max(buckets)))
fout.close()
