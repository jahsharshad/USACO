fin = open('backforth.in', 'r')
fout = open('backforth.out', 'w')

group1 = fin.readline().split()
group1 = [int(i) for i in group1]

group2 = fin.readline().split()
group2 = [int(i) for i in group2]

copy1 = group1
copy2 = group2


sums = [sum(group1)]

for a in range(10):
    for b in range(10):
        bucket1 = group1[a]
        bucket2 = group2[b]
        group1[a] = bucket2
        group2[b] = bucket1
        if sum(group1) not in sums:
            sums.append(sum(group1))

        for c in range(10):
            for d in range(10):
                bucket3 = group1[c]
                bucket4 = group2[d]
                group1[c] = bucket4
                group2[d] = bucket3
                if sum(group1) not in sums:
                    sums.append(sum(group1))

                group1[c] = bucket3
                group2[d] = bucket4

        group1[a] = bucket1
        group2[b] = bucket2

fout.write(str(len(sums)))
fout.close()
        
