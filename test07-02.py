aa = []
bb = []
val = 0

for i in range(0, 200):
    aa.append(val)
    val += 3

for i in range(0, 200):
    bb.append(aa[199-i])

print("bb[0]에는 %d, bb[199]에는 %d 입력됩니다." % (bb[0], bb[199]))
