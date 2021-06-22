import sys
fin = sys.stdin
fout = sys.stdout

nums = fin.readline().split()
nums = [int(i) for i in nums]
nums.sort()

sum = (sum(nums))/4
breaker = False

for x in range(7):
    a = nums[x]
    for y in range(x+1, 7):
        b = nums[y]
        for z in range(y+1, 7):
            c = nums[z]
            if (a+b+c) == sum:
                breaker = True
                break
        if breaker:
            break
    if breaker:
        break

final = str(a)+' '+str(b)+' '+str(c)
fout.write(final)
fout.close()
