## 변수 선언 부분 ##
i, hap, num1, num2 = 0, 0, 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    num1 = int(input("첫 번째 수 : "))
    num2 = int(input("두 번째 수 : "))

    for i in range(num1, num2+1):
        if i % 2 == 1:
            hap += i
    print("%d와 %d 사이에 있는 홀수의 합 : %d" % (num1, num2, hap))
