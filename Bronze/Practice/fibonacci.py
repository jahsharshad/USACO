fin = open('fibonacci.in', 'r')
fout = open('fibonacci.out', 'w')

n = int(fin.readline())

first = 1
second = 1
third = 0
y = 2

while 1 > 0:
    if n == 1:
        fout.write(str(1))
        break
    if n == 2:
        fout.write(str(2))
        break
    first = first+second
    y += 1
    if y == n:
        fout.write(str(first))
        break

    second = first+second
    y += 1
    if y == n:
        fout.write(str(second))
        break
fout.close()

