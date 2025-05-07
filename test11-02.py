inFp = None
inList, inStr = [], ""
num = 1

inFp = open("sample.txt", "r")

inList = inFp.readlines()
for inStr in inList:
    print("%d : %s" % (num, inStr), end="")
    num += 1

inFp.close()