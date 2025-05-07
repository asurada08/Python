import os

inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명을 입력하세요 :")

if os.path.exists(fName):
    inFp = open(fName, "r")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end="")
    
    inFp.close()
else:
    print("%s 파일이 없습니다." % fName)
'''
ex11-05.py 을 실행 했을 때 없는 파일을 열면 오류 발생함.
FileNotFoundError: [Errno 2] No such file or directory: 'aaa.txt'
os.path.exists(파일명) 형식 사용으로 예외 처리

1행 : os 모듈 import
8행 : 파일이 있으면 9~15행 수행, 파일이 없으면 17행 수행
'''