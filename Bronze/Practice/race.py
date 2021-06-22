# fin = open('race.in', 'r')
# fout = open('race.out', 'w')

# info = fin.readline()
info = [10, 5]
k = int(info[0])
n = int(info[1])
xs = [1, 2, 3, 4, 5]
# for i in range(n):
#     xs.append(int(fin.readline()))

meters = 0

for i in range(n):
    meters = 0
    speeds = []
    x = xs[i]
    speed = 1
    while meters < k:
        speeds.append(speed)
        if speed >= x and meters < k:
            speeds.append(speed)
            meters += speed
        meters += speed
        speed += 1
    print(str(speeds))

