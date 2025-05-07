## 변수 선언 부분 ##
i, dan = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    dan = int(input("출력할 단 : "))

    for i in range(9, 0, -1):
        print("%d * %d = %2d" % (i, dan, i*dan))
