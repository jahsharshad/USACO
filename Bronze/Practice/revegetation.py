fin = open('revegetate.in', 'r')
fout = open('revegetate.out', 'w')

info = fin.readline().split()
n = int(info[0])
m = int(info[1])
pairs = []
digits = [1]*n

for i in range(m):
    line = fin.readline().split()
    line = [int(i) for i in line]
    line.sort()
    pairs.append(line)
    
pairs.sort()


for i in range(2):
    for b in range(len(pairs)):
        num1 = pairs[b][0]
        num2 = pairs[b][1]
        digit1 = digits[num1-1]
        digit2 = digits[num2-1]
        if digit1 == digit2:
            digits[num2-1] += 1


for dig in digits:
    fout.write(str(dig))

fout.close()
