## 변수 전언 부분 ##
i, j, heartNum = 0, 0, 0
numStr, ch, heartStr = "", "", ""

## 메인 코드 부분 ##
if __name__ == "__main__":
    numStr = input("숫자를 여러개 입력하세요 : ")
    print()
    i=0
    ch = numStr[i]
    while True:
        heartNum = int(ch)

        heartStr = ""
        for j in range(0, heartNum):
            heartStr += "\u2665"
            j += 1
        print(heartStr)

        i += 1
        if(i > len(numStr)-1):
            break

        ch = numStr[i]
