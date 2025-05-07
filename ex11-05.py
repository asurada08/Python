inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명을 입력하세요 :")
inFp = open(fName, "r")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")
    
inFp.close()
'''
4행 : 파일명 입력(폴도 경로는 /로 입력)
5행 : open() 함수의 매개변수 중 파일 부분을 4행에서 입력받은 파일명(fName)으로 함
'''