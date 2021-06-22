fin = open('sumall.in', 'r')
fout = open('sumall.out', 'w')

numlist = fin
numlist = [int(i) for i in numlist]
sumlist = sum(numlist)-numlist[0]
fout.write(str(sumlist))
fout.close()
