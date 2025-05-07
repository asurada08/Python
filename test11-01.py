inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("sample.txt", "r")

i = 1
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d : %s" % (i, inStr), end = "")
    i += 1
    
inFp.close()

