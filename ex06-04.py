## 변수 선언 부분 ##
i, hap = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    num = int(input("1부터 어디까지 구할까요 : "))
    for i in range(1, num+1):
        hap += i
    print("1부터 %d까지 합 : %d" % (num, hap))
