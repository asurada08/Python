## 변수 선언 부분 ##
i, hap = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    for i in range(1, 101):
        hap += i

        if hap >= 1000:
            break
    print("1부터 100까지 합계를 최초로 1000이 넘어가게 하는 수 : %d" % i)
