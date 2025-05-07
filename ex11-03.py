inFp = None
inList = ""
'''
inFp = open("sample.txt", "r")

inList = inFp.readlines()
print(inList)

inFp.close()

6행 : 한번에 읽어서 inList에 저장
'''
with open("sample.txt", "r") as inFp:
    inList = inFp.readlines()
    print(inList)