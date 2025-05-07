## 변수 선언 부분 ##
hap, num1, num2, num3 = 0, 0, 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    num1 = int(input("시작값 : "))
    num2 = int(input("끝  값 : "))
    num3 = int(input("증가값 : "))
    '''
    for i in range(num1, num2+1, num3):
        hap += i
    print("%d에서 %d까지 %d씩 증가시킨 값의 합 : %d" % (num1, num2, num3, hap))
    '''
    i = num1
    while i < num2+1:
        hap = hap + i
        i = i + num3
    print("%d에서 %d까지 %d씩 증가시킨 값의 합 : %d" % (num1, num2, num3, hap))
    
