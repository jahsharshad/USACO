fin = open('fileio.in', 'r')
fout = open('fileio.out', 'w')

num = fin.readline()

fout.write(num)
fout.close()
