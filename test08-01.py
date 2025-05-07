'''
"파이썬은완전재미있어요"를 파#썬#완#재#있#요 로 출력
짝수번째글은 그대로 홀수번째 글은 #이 표시
'''
ss = "파이썬은완전재미있어요"
sslen = len(ss)
for i in range(0, sslen):
    if i%2==0:
        print(ss[i],end="")
    else:
        print("#",end="")
print()
ss1 = "파이썬은완전재미있어요"
ss1len = len(ss1)
for i in range(0, ss1len):
    if i % 3 == 0:
        print(ss1[i],end="")
    else:
        print("#",end="")
