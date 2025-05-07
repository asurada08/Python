'''
딕셔너리 개념
 - 쌍 2개가 하나로 묶인 자료구조
  ex) apple:사과 처럼 의미 있는 두 값을 연결해 구성
 - 중괄호{}로 묶어 구성, 키(Key)와 값(Value)의 쌍으로 구성
 연관 메모리, 연관배열이 파이썬에선 딕셔너리
'''
## 딕셔너리 생성
dic1 = {1:'A',2:'B',3:'C',4:'D'}
print("dic1 :",dic1, type(dic1))
## 키와 값을 반대로 : 키와 값은 사용자가 지정 규정 없음
dic2 = {'A':1,'B':2,'C':3,'D':4}
print("dic2 :",dic2, type(dic2))
## 여러 정보의 딕셔너리 표현
student1 = {"학번":1000,"이름":"홍길동","학과":"컴퓨터학과"}
print("student1 :",student1, type(student1))
## 딕셔너리 키:값 추가
student1['연락처']='010-1234-5678'
print("student1 :",student1, type(student1))
## 딕셔너리 키:값 수정
student1['학과']='기계공학과'
print("student1 :",student1, type(student1))
## 딕셔너리 키:값 삭제
del(student1['학과'])
print("student1 :",student1, type(student1))
## 동일한 키를 갖는 딕셔너리를 생성하는 것이 아니라 마지막에 있는 키 적용됨
student1 = {"학번":1000,"이름":"홍길동","학과":"컴퓨터학과","학번":1001}
print("student1 :",student1, type(student1))

## 딕셔너리의 사용
## 키로 값에 접근하는 코드
print("student1['학번'] :", student1['학번'])
print("student1['이름'] :", student1['이름'])
print("student1['학과'] :", student1['학과'])
## 딕셔너리명.get(키) 함수 사용해 키로 값에 접근
print("student1.get('이름') :", student1.get('이름'))
## 위에 두가지 방법 결과 같음
## 딕셔너리명[키]는 없는 키 호출하면 오류, 딕셔너리명.get(키)는 아무것도 반환 안함
## print("student1['주소'] :", student1['주소']) : KeyError: '주소'
print("student1.get('주소') :", student1.get('주소')) ##student1.get('주소') : None
## 딕셔너리명.keys()는 모든 키 반환
print("student1.keys() :", student1.keys())
## dict_keys(['학번', '이름', '학과']) dict_keys 빼려면
print("list(student1.keys()) :", list(student1.keys()))
## 딕셔너리명.values() 모든 값 반환
print("student1.values() :", student1.values())
print("list(student1.values()) :", list(student1.values()))
## 튜플형태로 값 반환
print("student1.items()", student1.items())
print("list(student1.items())", list(student1.items()))
## 딕셔너리 안에 해당 키가 있는지 없는지 확인(in)
print("이름" in student1)
print("주소" in student1)
