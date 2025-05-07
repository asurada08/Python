inFp, outFp = None, None
inStr = ""
'''
inFp = open("test1.txt", "r")
outFp = open("test2.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("파일이 정상적으로 복사 되었음")
'''

with open("test1.txt", "r") as inFp:
    with open("test2.txt", "w") as outFp:
        for inStr in inFp:
            outFp.writelines(inStr)
print("파일이 정상적으로 복사 되었음")
'''
4~5행 : 읽기 및 쓰기 모드로 파일 열기
7행 : 파일의 내용을 통째로 읽기
8~9행 : 내용을 쓰기 파일에 쓰기
11~12행 : 파일 닫기
'''
