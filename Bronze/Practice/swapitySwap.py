fin = open('swap.in', 'r')
fout = open('swap.out', 'w')

line1 = fin.readline().split()
n = int(line1[0])
k = int(line1[1])

nums = [b for b in range(1, n+1)]
numsCopy = nums

numList = []

rank = 0

line2 = fin.readline().split()
a1 = int(line2[0])
a2 = int(line2[1])

line3 = fin.readline().split()
b1 = int(line3[0])
b2 = int(line3[1])

if k % 2 == 0:
    odd = False
else:
    odd = True

if (a2 < b1) or (b2 < a1) or (b1 > a1 and b2 < a2 and b1-a1 == a2-b2) or (a1 > b1 and a2 < b2 and a1-b1 == b2-a2):
    if odd:
        reverse1 = nums[a1 - 1:a2]
        reverse1.reverse()
        nums[a1 - 1:a2] = reverse1

        reverse2 = nums[b1 - 1:b2]
        reverse2.reverse()
        nums[b1 - 1:b2] = reverse2
else:
    for i in range(k):
        reverse1 = nums[a1-1:a2]
        reverse1.reverse()
        nums[a1-1:a2] = reverse1

        reverse2 = nums[b1 - 1:b2]
        reverse2.reverse()
        nums[b1-1:b2] = reverse2

        if k > 1000:
            if nums in numList:
                rank = numList.index(nums)
                rank += 1
                diff = i - rank
                total = k
                total -= rank
                nums = numList[(total % diff)+diff]
                break
            else:
                numList.append(nums)


for num in nums:
    fout.write(str(num))
    if nums.index(num) != (len(nums)-1):
        fout.write('\n')

fout.close()
