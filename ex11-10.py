inFp, outFp = None, None
inStr = ""

inFp = open("c:/Windows/notepad.exe", "rb")
outFp = open("test2.txt", "wb")

while True:
    inStr = inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("파일이 정상적으로 복사 되었음")
'''
이진 파일의 복사
4~5행 : 이진 읽기 모드와 쓰기 모드로 파일 열기
7~11행 : 파일의 끝까지 한 바이트씩 읽어서 한 바이트씩 파일에 쓰기
'''