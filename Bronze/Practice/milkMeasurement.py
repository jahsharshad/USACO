fin = open('measurement.in', 'r')
fout = open('measurement.out', 'w')

length = int(fin.readline())
bessie = 7
elsie = 7
mildred = 7
bestMax = 7
changeNum = 0
toppers = []
topCow = ''

log = {}

for i in range(length):
    line = fin.readline().split()
    number = int(line[0])
    name = line[1]
    change = int(line[2])
    log[number] = [name, change]

log = sorted(log.items())
log = [list(x) for x in log]

for i in range(length):
    entry = log[i]
    cow = entry[1][0]
    change = entry[1][1]

    if cow == 'Bessie':
        bessie += change
        possibleMax = bessie
    elif cow == 'Elsie':
        elsie += change
        possibleMax = elsie
    elif cow == 'Mildred':
        mildred += change
        possibleMax = mildred

    newToppers = []
    currentMax = max(bessie, elsie, mildred)
    if bessie == currentMax:
        newToppers.append('Bessie')
    if elsie == currentMax:
        newToppers.append('Elsie')
    if mildred == currentMax:
        newToppers.append('Mildred')

    if newToppers != toppers:
        changeNum += 1
    toppers = newToppers


fout.write(str(changeNum))
fout.close()

