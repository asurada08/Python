hap = 0
a, b = 0, 0

while True:
    a = int(input("더할 첫 번째 수 : "))
    if a == "$":
        break
    b = int(input("더할 두 번째 수 : "))
    hap = a + b
    print("%d + %d = %d" %(a, b, hap))
