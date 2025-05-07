## 변수 선언 부분 ##
answer, num1, num2, num3 = 0, 0, 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        num3 = int(input("더할 숫자를 입력하세요 :"))
        for num3 in range(num1, num2 + 1, num3):
            answer = answer + num3
        print("%d+...+%d는 %d 입니다." % (num1, num2, answer))
    
