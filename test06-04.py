## 변수 선언 부분 ##
i, j, dan = 0, 0, ""

## 메인 코드 부분 ##
if __name__ == "__main__":
    for i in range(9, 1, -1):
        dan += "    %d단     " % i
    print(dan)

    for i in range(9, 0, -1):
        dan = ""
        for j in range(9, 1, -1):
            dan += str("%2d * %2d = %2d" % (j, i, j*i))
        print(dan)
