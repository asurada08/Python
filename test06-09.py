i, j, num = 0, 0, 0

num = int(input("숫자를 입력하세요 :"))
for i in range(0, num):
    for j in range(num, i, -1):
        print("*",end="")
    print("")

i, j, k, num = 0, 0, 0, 0
num = int(input("숫자를 입력하세요 :"))
for i in range(0, num):
    for j in range(num-1, i, -1):
        print(" ",end="")
    for k in range(0, i+1):
        print("*",end="")
    print("")

i, j, k, num = 0, 0, 0, 0
num = int(input("숫자를 입력하세요 :"))
for i in range(num, 0, -1):
    for j in range(0, num-i):
        print(" ",end="")
    for k in range(1, i*2):
        print("*",end="")
    print("")
