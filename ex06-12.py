hap = 0
a, b = 0, 0

while True:
    a = int(input("더할 첫 번째 수 : "))
    if a == -1:
        break
    b = int(input("더할 두 번째 수 : "))
    hap = a + b
    print("%d + %d = %d" %(a, b, hap))
print("-1을 입력해 반복문 탈출")
