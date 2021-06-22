fin = open('notlast.in', 'r')
fout = open('notlast.out', 'w')

numLine = int(fin.readline())
cows = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle', 'Maggie', 'Henrietta']
milks = [0, 0, 0, 0, 0, 0, 0]

fout.write('')

for i in range(numLine):
    line = fin.readline().split()
    cow = line[0]
    milk = int(line[1])
    position = cows.index(cow)
    milks[position] += milk

last = min(milks)
lastPlaces = []

for i in range(7):
    if milks[i] == last:
        lastPlaces.append(i)

downer = 0
for place in lastPlaces:
    del(milks[place - downer])
    del(cows[place - downer])
    downer += 1


if not cows:
    fout.write('Tie')
    fout.close()
elif milks.count(min(milks)) > 1:
    fout.write('Tie')
    fout.close()
else:
    secondLast = min(milks)
    position = milks.index(secondLast)
    fout.write(cows[position])
    fout.close()
