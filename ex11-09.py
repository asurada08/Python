## 변수 선언 부분 ##
inFp, outFp = None, None
inStr, outStr = "", ""
i, secu = 0, 0

## 메인 코드 부분 ##
secuYN = input("1.암호화 2.암호해석 중 선택 :")
inFname = input("입력 파일명을 입력하세요 :")
outFname = input("출력 파일명을 입력하세요 :")

if secuYN == "1":
    secu = 100
elif secuYN == "2":
    secu = -100

inFp = open(inFname, "r", encoding = "utf-8")
outFp = open(outFname, "w", encoding= "utf-8")

while True:
    inStr = inFp.readline()
    if not inStr:
        break
    
    outStr = ""
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2
    
    outFp.write(outStr)

outFp.close()
inFp.close()
print("%s --> %s 변환 완료" % (inFname, outFname))
'''
7행 : 수행할 작업이 암호화 인지 암호 해독인지 입력
16~17행 : 파일을 열 때 인코딩을 utf-8로 지정
11~14행 : secu 변수값이 암호화 할 때는 100으로 설정 암호 해독할때는 -100으로 설정
19~32행 : 입력 파일의 끝까지 읽으면서 무한 반복
21행 : inStr에 읽어 온 것이 아무것도 없으면 22행이 실행되어서 while 문 빠져나감
24행 : outStr은 한 행을 암호화 한 결과 저장하는 변수
25~30행 : 읽어 온 행의 글자 개수만큼 반복
26행 : 글자 하나씩 추출 후 27행에서 글자를 숫자로 변환
28행 : 100 또는 -100을 더한 후 29행에서 다시 글자로 변환, 이 글자를 outStr에 추가
outStr은 한 행을 암호화, 암호 해독한 문자열 저장
32행 : 암호화 또는 암호를 해독한 내용을 파일에 씀
'''