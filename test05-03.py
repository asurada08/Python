## 변수 선언 부분 ##
num1,res = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    num1 = int(input("숫자를 입력하세요 : "))
    for i in range(2, num1):
        if num1 % i == 0:
            res = 1    
    if res == 0:
        print("%d는 소수 입니다" % num1)
    else:
        print("%d는 소수가 아닙니다" % num1)
