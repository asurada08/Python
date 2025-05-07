inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("sample.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end = "")
    
inFp.close()
'''
6~10행 : 무한 반복
7행 : 파일에서 행을 1개 읽음
8행 : 읽어 온 것이 없다면 9행 break로 무한 반복에서 벗어남
10행 : 그렇지 않으면 읽어온 내용 출력
'''