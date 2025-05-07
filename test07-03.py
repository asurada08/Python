list1 = []
list2 = []
val = 0
for i in range(0, 4):
    for j in range(0, 5):
        list1.append(val)
        val += 3
    list2.append(list1)
    list1 = []

for i in range(0, 4):
    for j in range(0, 5):
        print("%3d" % list2[i][j], end="")
    print("")
