fin = open('highcard.in', 'r')
fout = open('highcard.out', 'w')


lineNum = int(fin.readline())
elsie = []
bessie = []
points = 0

for i in range(lineNum):
    card = int(fin.readline())
    elsie.append(card)

for i in range(2*lineNum):
    if i+1 not in elsie:
        bessie.append(i+1)

elsie.sort()
bessie.sort()

while bessie:
    curBessie = bessie.pop(0)
    if curBessie > elsie[0]:
        points += 1
        elsie.pop(0)
           

fout.write(str(points))
fout.close()


