fin = open('sleepy.in', 'r')
fout = open('sleepy.out', 'w')

numChar = int(fin.readline())
order = fin.readline().split()
order = [int(i) for i in order]
ans = 0
for i in range(numChar-2, -1, -1):
    if order[i] > order[i+1]:
        ans = i+1
        break
fout.write(str(ans))
fout.close()
