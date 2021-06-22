import sys
fin = sys.stdin
fout = sys.stdout

# fin = open('1.in', 'r')
# fout = open('oddphoto.out', 'w')

nums = int(fin.readline())
ints = fin.readline().split()

ints = [int(i) for i in ints]

even = 0
odd = 0
groups = 0

for i in ints:
    if (i % 2) == 0:
        even += 1
    elif (i % 2) == 1:
        odd += 1

if even > odd:
    groups = (odd*2)+1
elif odd == even:
    groups = nums
elif odd > even:
    nums -= even*2
    groups += even*2

    if (nums % 3) == 1:
        groups += 2
        nums -= 5
    if (nums % 3) == 2:
        groups += 1
        nums -= 2
    if (nums % 3) == 0:
        groups += (nums/3)*2
        nums = 0

fout.write(str(int(groups)))
fout.close()
