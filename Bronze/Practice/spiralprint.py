fin = open('spiralprint.in', 'r')
fout = open('spiralprint.out', 'w')

list_length = int(fin.readline())
int_list = []


for w in range(list_length):
    int_list.append(fin.readline())

for q in range(len(int_list)):
    int_list[q] = int_list[q].split()


global i
global j
global x

i = 1
j = 0
x = 0

for q in range(list_length):
    j += 1
    fout.write(int_list[i-1][j-1])
    fout.write('\n')
    x += 1


loop_length = list_length
global m
global n
m = 0
n = 1

while 1 > 0:
    loop_length -= 1

    for q in range(loop_length):
        j += m
        i += n
        fout.write(int_list[i-1][j-1])
        fout.write('\n')
        x += 1

    if x == list_length**2:
        break

    n *= -1

    for q in range(loop_length):
        j += n
        i += m
        fout.write(int_list[i-1][j-1])
        fout.write('\n')
        x += 1

    if x == list_length**2:
        break


fout.close()
