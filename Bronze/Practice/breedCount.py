fin = open('bcount.in', 'r')
fout = open('bcount.out', 'w')

info = fin.readline().split()
n = int(info[0])
q = int(info[1])
breeds = [[0, 0, 0]]
count = [0, 0, 0]

for a in range(n):
    breed = int(fin.readline())
    count[breed-1] += 1
    breeds.append(count.copy())

for d in range(q):
    line = fin.readline().split()
    a = int(line[0])
    b = int(line[1])
    count1 = breeds[a-1]
    count2 = breeds[b]
    a1 = count1[0]
    a2 = count2[0]
    b1 = count1[1]
    b2 = count2[1]
    c1 = count1[2]
    c2 = count2[2]
    fout.write(str(a2-a1)+' '+str(b2-b1)+' '+str(c2-c1))
    if d != (q-1):
        fout.write('\n')

fout.close()

