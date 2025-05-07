inFp, outFp = None, None
inStr = ""

sfName = input("소스 파일명을 입력하세요 : ")
inFp = open(sfName, "r")
tfName = input("타겟 파일명을 입력하세요 : ")
outFp = open(tfName, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("%s 파일이 %s 정상적으로 복사 되었음" % (sfName, tfName))