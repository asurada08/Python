'''
문자열을 입력받아, 꺼꾸로 출력하시오
출력형식)
문자열 입력 : python fun!!
문자열 출력 : !!nuf nohtyp
'''
## 변수 선언 부분
str1 = ""

## if문 사용
## for문 사용 (for 제어변수 in 컬렉션 :)
if __name__ == "__main__":
    str1 = input("문자열 입력 : ")
    for i in range(len(str1)-1,-1,-1):
        print("%c" % str1[i], end="")

