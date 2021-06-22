fin = open('gymnastics.in', 'r')
fout = open('gymnastics.out', 'w')

length = fin.readline()
length = length.split()
height = int(length[0])
width = int(length[1])
wholeList = []
rowList = []
consistentList = []



for i in range(height):
    currentList = fin.readline()
    currentList = currentList.split()
    wholeList.append(currentList)

for i in range(height):
    tempList = wholeList[i]
    for q in range(width-1):
        for x in range(width-(q+1)):
            consistent = [tempList[q], tempList[q+x+1]]
            rowList.append(consistent)
    if i == 0:
        consistentList = rowList

removeList = []

for m in range(len(consistentList)):
    count = consistentList.count(consistentList[m])
    if count != height:
        for i in range(count):
            removeList.append(consistentList[m])

for d in range(len(removeList)):
    if consistentList.count(removeList[d]) > 0:
        consistentList.remove(removeList[d])

out = len(consistentList)/height
fout.write(str(int(out)))
fout.close()





