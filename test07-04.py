tt = ((1, 2, 3),(4, 5, 6),(7, 8, 9))

for i in tt:
    for j in i:
        print(j, end=" ")
    print()

for i in range(len(tt)):
    for j in range(len(tt[i])):
        print(tt[i][j], end=" ")
    print()

i = 0
while i <len(tt):
    x, y, z = tt[i]
    print(x, y, z)
    i += 1
