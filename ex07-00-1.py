## 튜플 생성
## ()로 생성, ()생략 가능, 튜플은 값 수정할 수 없음, 읽기전용
tt1 = (10, 20, 30); print("tt1 :", tt1, type(tt1))
tt2 = 10, 20, 30; print("tt2 :", tt2, type(tt2))
tt3 = (10); print("tt3 :", tt3, type(tt3))
tt4 = 10; print("tt4 :", tt4, type(tt4))
## 항목이 1개인 튜플은 쉼표(,) 붙임
tt5 = (10,); print("tt5 :", tt5, type(tt5))
tt6 = 10,; print("tt6 :", tt6, type(tt6))
## 튜플 오류 / 추가, 삽입, 값 삭제 불가
'''
tt1.append(40) 'tuple' object has no attribute 'append'
tt1[0]=40 'tuple' object does not support item assignment
del(tt1[0]) 'tuple' object doesn't support item deletion
'''
## 튜플 삭제 / 튜플 전체 삭제 가능
tt7 = 1, 2, 3
print("tt7 :", tt7, type(tt7))
del(tt7)

## 튜플 사용 (리스트랑 같음)
## 튜플 항목에 접근
tt8 = 10, 20, 30, 40
print("tt8[0] :", tt8[0], type(tt8[0]))
print("tt8[0]+tt8[1]+tt8[2] :", tt8[0]+tt8[1]+tt8[2])
## 튜플 범위에 접근
print("tt8[1:3] :", tt8[1:3])
print("tt8[1:] :", tt8[1:])
print("tt8[:3] :",tt8[:3])
## 튜플의 덧셈 및 곱셈 연산
tt9 = ('A', 'B')
print("tt8 + tt9 :", tt8+tt9)
print("tt9 * 3 :", tt9*3)

## 튜플 -> 리스트 -> 튜플 변환
myTuple = (10, 20, 30)
print("myTuple :",myTuple, type(myTuple))
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print("myTuple :",myTuple, type(myTuple))
