inFp = None
inList, inStr = [], ""

inFp = open("sample.txt", "r")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")
    
inFp.close()