aa = [0, 0, 0, 0]
hap = 0

for i in range(0, 4):
    aa[i] = int(input("%d번 숫자 : " % (i+1)))

    hap += aa[i]

print("합계 : %d" % hap)
