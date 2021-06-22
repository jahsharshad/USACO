fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')

line1 = fin.readline()
line1 = line1.split()
cap1 = int(line1[0])
amount1 = int(line1[1])

line2 = fin.readline()
line2 = line2.split()
cap2 = int(line2[0])
amount2 = int(line2[1])

line3 = fin.readline()
line3 = line3.split()
cap3 = int(line3[0])
amount3 = int(line3[1])

for i in range(1, 101):
    state = i % 3
    if state == 1:
        change1 = min(amount1, cap2-amount2)
        amount1 -= change1
        amount2 += change1
    elif state == 2:
        change2 = min(amount2, cap3-amount3)
        amount2 -= change2
        amount3 += change2
    elif state == 0:
        change3 = min(amount3, cap1-amount1)
        amount3 -= change3
        amount1 += change3

fout.write(str(amount1)+'\n')
fout.write(str(amount2)+'\n')
fout.write(str(amount3))
fout.close()
