inStr = "<<<<파<<이>>썬>>>>"
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != "<" and inStr[i] != ">":
        outStr += inStr[i]
    
print("원래 문자열 :", '['+inStr+']')
print("수정 문자열 :", '['+outStr+']')
