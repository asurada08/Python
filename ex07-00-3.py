## 리스트, 튜플, 딕셔너리 심화
## 세트(set) : 키만 모아 놓은 딕셔너리의 특수한 형태
## 딕셔너리의 키는 중복되면 안 되므로 세트에 들어있는 값은 항상 유일
## 세트를 생성하려면 딕셔너리처럼 중괄호{} 사용하지만 : 없이 값 입력

## 중복되는 것은 자동으로 하나만 남음
mySet1 = {1,1,2,2,3,3,4,4}
print("mySet1 :",mySet1)

## 종류만 파악하고 싶을 때
salesList = ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락','바나나']
print("salesList :",set(salesList))

## 두 세트 사이의 교집합, 합집합, 차집합, 대칭 차집합을 구할 때
mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}
print("mySet1 & mySet2 :",mySet1 & mySet2)
print("mySet1 | mySet2 :",mySet1 | mySet2)
print("mySet1 - mySet2 :",mySet1 - mySet2)
print("mySet1 ^ mySet2 :",mySet1 ^ mySet2)
## 연산자 대신 함수 사용
print("mySet1.intersection(mySet2) :",mySet1.intersection(mySet2))
print("mySet1.union(mySet2) :",mySet1.union(mySet2))
print("mySet1.difference(mySet2) :",mySet1.difference(mySet2))
print("mySet1.symmetric_difference(mySet2) :",mySet1.symmetric_difference(mySet2))

## 컴프리헨션 : 값이 순차적인 리스트를 한 줄로 만드는 간단한 방법
## 1~5 까지 저장된 리스트
numList=[]
for num in range(1, 6):
    numList.append(num)
print("numList :", numList)
## 위에 내용을 컴프리헨션으로
numList1 = [num for num in range(1,6)]
print("numList1 :", numList1)
'''
컴프리헨션의 구성
리스트 = [수식 for 항목 in range() if 조건식]
'''
## 1~5 제곱으로 구성된 리스트
numList2 = [num*num for num in range(1,6)]
print("numList2 :", numList2)

## 1~20 숫자 중에 3의 배수로 구성된 리스트
numList3 = [num for num in range(1,21) if num % 3 == 0]
print("numList3 :", numList3)

## 동시에 여러 리스트에 접근
## zip() 함수를 사용해 동시에 여러 리스트에 접근
foods = ['떡볶이', '자장면','라면','피자','맥주','치킨','삼겹살']
sides = ['오뎅','단무지','김치']
for food,side in zip(foods,sides):
    print(food, ':', side)

## 두 리스트를 튜플이나 딕셔너리로 짝지을 때 zip() 함수 사용
foods = ['떡볶이', '자장면','라면','피자','맥주','치킨','삼겹살']
sides = ['오뎅','단무지','김치']
tupList = list(zip(foods, sides))
dic = dict(zip(foods, sides))
print("tupList :", tupList)
print("dic :", dic)

## 리스트 복사
## 얕은복사 : newList=oldList는 동일한 메모리 공간 공유
oldList=['자장면','짬뽕','탕수육']
newList=oldList
print("newList :",newList)
oldList[2]='볶음밥'
oldList.append('군만두')
print("newList :",newList)
print("id 비교 :",id(newList), id(oldList))
## 깊은복사 : newList=oldList[:]는 메모리의 공간을 복사해서 새로 만듬(얕은복사방지)
oldList=['자장면','짬뽕','탕수육']
newList=oldList[:]
print("newList :", newList)
oldList[2]='볶음밥'
oldList.append('군만두')
print("newList :", newList)
print("oldList :", oldList)
print("id 비교 :",id(newList), id(oldList))
## 리스트를 이용한 스택 구현(후입선출)
parking=[]
top = 0
print("parking", parking)
parking.append("캐스퍼")
top += 1
print("parking", parking)
parking.append("카니발")
top += 1
parking.append("스타렉스")
top += 1
print("parking", parking)
top -= 1
outCar=parking.pop()
print("parking", parking)
top -= 1
outCar=parking.pop()
print("parking", parking)
