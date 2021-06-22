fin = open('cowsignal.in', 'r')
fout = open('cowsignal.out', 'w')

numbers = fin.readline()
numbers = numbers.split()
lines = int(numbers[0])
length = int(numbers[1])
times = int(numbers[2])
characterList = []

for i in range(lines):
    characterList.append(fin.readline())

for i in range(lines):
    currentString = characterList[i]
    smallString = ''
    for x in range(length):
        currentCharacter = currentString[x]
        smallString = smallString + currentCharacter*times
    for q in range(times):
        fout.write(smallString+'\n')

fout.close()


