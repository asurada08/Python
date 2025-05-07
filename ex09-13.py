import random

## 함수 선언 부분 ##
def getNumber(): # 함수 정의(4, 5)
    return random.randrange(1, 46) # 1~45 중에 임의의 숫자 하나 추출

## 전역변수 선언 부분 ##
lotto = [] # 추첨된 숫자를 저장할 리스트, 임시 저장할 num 변수 준비
num = 0

## 메인 코드 부분 ##
print("로또 추첨을 시작합니다 **\n");

while True: # 무한반복(14~21)
    num = getNumber()

    if lotto.count(num) == 0: # 이미 뽑힌 숫자가 리스트에 없어야 추가(17, 18)
        lotto.append(num)

    if len(lotto) >= 6:
        break

print("추첨된 로또 번호 : ", end = " ")
lotto.sort() # 숫자 6개 정렬
for i in range(0, 6):
    print("%d " % lotto[i], end = " ")
