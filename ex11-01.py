inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("D:\java_class\python_class\sample.txt", "r")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()
'''
4행 : 파일열기
6행 : readline() 함수는 inFp로 열린 파일에서 한 행 읽어 inStr에 저장
7행 : 화면에 출력
9~13행 : 반복
15행 : 파일닫기
6~13행 : 3줄만 읽어오게 해놔서 텍스트 파일에 줄이 1~2개만 있으면 오류 발생
         4줄 이상이여도 3줄만 읽어옴
'''