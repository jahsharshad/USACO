import re
fin = open('whereami.in', 'r')
fout = open('whereami.out', 'w')

length = int(fin.readline())
string = fin.readline()

if len(string) == 0:
    fout.write(str(0))
    fout.close()
    
for i in range(0, length):
    allcounts = []
    sublen = i
    end = length - sublen
    for q in range(0, end):
        sub = string[q:q+sublen+1]
        #count = string.count(sub)
        count = len(re.findall('(?='+sub+')', string))
        allcounts.append(count)
        if count > 1:
            break

    if max(allcounts) == 1:
        fout.write(str(sublen+1))
        fout.close()
        break




        

