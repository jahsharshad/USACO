fin = open('lostcow.in', 'r')
fout = open('lostcow.out', 'w')

line = fin.readline().split()
x = int(line[0])
y = int(line[1])

positions = []
num = x
change = 1
total = 0
while True:
    num = x + change
    if (change > 0 and num >= y and ((num-change) < y)) or (change < 0 and num <= y and ((num-change) > y)):
        positions.append(y)
        break
    else:
        positions.append(num)
        change *= -2

for x in range(len(positions)):
    currNum = positions[x]
    if x == 0:
        diff = 1
    else:
        diff = abs(positions[x-1]-currNum)
    total += diff

fout.write(str(total))

