## 문자열을 입력받아 그중 'o'를 '$'로 변경
ss = input("입력 문자열 :")

print("출력 문자열 :", end="")
for i in range(0, len(ss)):
    if ss[i] != 'o':
        print(ss[i],end="")
    else:
        print("$",end="")
