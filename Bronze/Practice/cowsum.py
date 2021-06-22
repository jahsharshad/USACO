fin = open('cowsum.in', 'r')
fout = open('cowsum.out', 'w')

bg = fin.readline()
bg = bg.split()
n = int(bg[0])
t = int(bg[1])
cowList = []

for i in range(int(n)):
    cowList.append(fin.readline())

for i in range(len(cowList)):
    cowList[i] = cowList[i].split()
    cowList[i] = [int(x) for x in cowList[i]]


class Cow:
    def __init__(self, weight, height, width, length, start, end):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.start = start
        self.end = end


attributes = {}
weightList = []
heightList = []
widthList = []
lengthList = []
maxWeight = -1
maxHeight = -1
maxWidth = -1
maxLength = -1

for i in range(len(cowList)):
    attributes['cow'+str(i+1)] = Cow(cowList[i][0], cowList[i][1], cowList[i][2], cowList[i][3], cowList[i][4], cowList[i][5])

    if not (attributes['cow'+str(i+1)].start <= t < attributes['cow'+str(i+1)].end):
        attributes['cow'+str(i+1)].weight = -1
        attributes['cow'+str(i+1)].height = -1
        attributes['cow'+str(i + 1)].width = -1
        attributes['cow' + str(i + 1)].length = -1

    if attributes['cow'+str(i+1)].weight > maxWeight:
        maxWeight = attributes['cow'+str(i+1)].weight
    if attributes['cow'+str(i+1)].height > maxHeight:
        maxHeight = attributes['cow'+str(i+1)].height
    if attributes['cow'+str(i+1)].width > maxWidth:
        maxWidth = attributes['cow'+str(i+1)].width
    if attributes['cow'+str(i+1)].weight > maxLength:
        maxLength = attributes['cow'+str(i+1)].length


fout.write(str(maxWeight)+'\n')
fout.write(str(maxHeight)+'\n')
fout.write(str(maxWidth)+'\n')
fout.write(str(maxLength)+'\n')

fout.close()




