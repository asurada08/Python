## 변수 선언 부분 ##
i, j = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    for i in range(2, 10):
        for j in range(1, 10):
            print("%d * %d = %2d" % (i, j, i*j))
        print("")
