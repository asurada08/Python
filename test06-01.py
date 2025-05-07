## 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    for i in range(0, 101):
        if i % 7 == 0:
            hap += i

    print("0 ~ 100 사이에 있는 7의 배수 합 : %d" % hap)
