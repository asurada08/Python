## 함수
## 함수 개념, 필요성
## 함수(Function) : 함수는 외부에 별도 존재 *함수명()
## 메서드(Method) : 메서드는 클래스 안에 존재 

## 지역변수, 전역변수
## 지역변수 : 한정된 지역에서만 사용
## 전역변수 : 프로그램 전체에서 사용

## global 예약어 : 전역변수로 지정

## 함수의 반환값 : return 문으로 반환 리턴값이라고도 함. 매개변수 = 파라미터

## pass 예약어 : 건너뜀?
## True 일 때 아무런 할 일이 없다고 빈줄로 둘 때 오류 발생
## expected an indented block after 'if' statement on line 17
'''
if True:
    pass
else:
    print("거짓이네요")
'''
## 함수 호출할 때 딕셔너리 형식의 매개변수를 키 = 값 형식으로 사용 ##
'''
def dic_func(**para):
    for k in para.keys():
        print("%s : %d명 입니다" % (k, para[k]))

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)
'''
## 모듈 : 함수의 집합
## 모듈 파일 작성 다른 파일에 import 모듈명 하면 모듈파일의 함수 사용 가능
'''
방법1
import 모듈명

방법2
from 모듈명 import 함수1, 함수2, 함수3
or
from 모듈명 import *
'''
'''
모듈의 종류
표준 모듈, 사용자 정의 모듈, 서드 파티 모듈로 구분
표쥰 모듈 : 파이썬에서 제공하는 모듈
사용자 정의 모듈 : 직접 만들어서 사용하는 모듈
서드 파티 모듈(3rd Party) : 파이썬이 아닌 외부 회사나 단체에서 제공하는 모듈
 : 파이썬 표준 모듈이 모든 기능을 제공하지 않음
 : 서드 파티 모듈 덕분에 파이썬에서도 고급 프로그래밍 가능
 : 게임 개발 기능이 있는 pyGame, 윈도우창을 제공하는 PyGTK, 데이터베이스 기능의 SQLAlchemy 등
'''
## 파이썬에서 제공하는 표준 모듈의 목록을 일부 확인
'''
import sys
print("sys : ", sys.builtin_module_names)
'''
## dir(__builtins__) 명령어로도 제공하는 모듈과 예약어 확인
'''
import math
dir(math)
'''

## 파이썬에서 Call By Value, Call By Reference
'''
값에 의한 전달(Call By Value)
 : 값에 의한 전달은 일반 변수나 값을 전달할 때 함수에 동일한 크기의 별도의 메모리
   공간이 확보되어 값이 복사되는 방식

def func(p): # p는 별도의 메모리 공간을 확보함
    p = 222
v = 111
func(v)
print(p) # 111이 출력됨

참조에 의한 전달
 : 참조에 의한 전달은 리스트*를 매개변수로 전달하므로 주소가 전달되어 메모리
   공간이 공유되는 방식. 함수에서 리스트를 변경하면 메인코드의 리스트도 변경됨

def func(p): # 리스트 p는 리스트 v와 메모리를 공유함
    p[0] = 222
v = [111]
func(v)
print(v[0]) # 222가 출력됨
#리스트* : 튜플, 딕셔너리, 세트도 해당됨
'''

## 패키지 : 모듈이 하나의 파일 안에 함수가 여러개 들어있는 것이라면
##          패키지는 여러 모듈을 모아 놓은 것으로 폴더의 형태로 나타냄
##          모듈을 주제별로 분리할 때 주로 사용
## import 형식 : from 패키지명.모듈명 import 함수명

## 내부함수(lambda, map()) : 함수 안에 함수가 있는 형태
'''
def outFunc(v1, v2):
    def inFunc(num1, num2):
        return num1 + num2
    return inFunc(v1, v2)
print(outFunc(10, 20)) # 30 출력됨
'''
## outFunc() 함수 밖에서 호출하면 오류 발생
## NameError : name 'inFunc' is not defined

## 람다 함수(lambda) : 함수를 한 줄로 간단하게 만들어줌
'''
def hap(num1, num2):
    res = num1 + num2
    return res
print(hap(10, 20)) # 30 출력
'''
## 위의 함수를 람다 함수로 작성
'''
hap2 = lambda num1, num2 : num1 + num2
print(hap2(10, 20))
'''
## 매개변수에 기본값을 설정
## 매개변수를 지정하지 않으면 기본값으로 설정, 매개변수를 넘겨주면 기본값 무시
''' 
hap3 = lambda num1 = 10, num2 = 20 : num1 + num2
print(hap3())
print(hap3(100, 200))

'''
## 리스트에 모두 10을 더하는 코드
''' 
myList = [1, 2, 3, 4, 5]
def add10(num):
    return num + 10

for i in range(len(myList)):
    myList[i] = add10(myList[i])
print(myList)
'''
## 람다함수와 map() 함수로 간단히
## lambda(인자 : 표현식)
## map(function : 각 요소에 적용할 함수, iterable : 함수를 적용할 데이터 집합)
''' 
myList = [1, 2, 3, 4, 5]
add10 = lambda num : num + 10
myList = list(map(add10, myList))
print(myList)
'''
## 2행, 3행을 합침
''' 
myList = [1, 2, 3, 4, 5]
myList = list(map(lambda num : num +10, myList))
print(myList)
'''
## 두 리스트의 각 자리수를 합쳐서 새로운 리스트로 만들기
'''
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
hapList = list(map(lambda n1, n2 : n1 + n2, list1, list2))
print(hapList)
'''
## filter(), sorted(), reduce() 함수 들도 lambda()와 사용할 수 있다

## filter() : 시퀀스(리스트, 튜플 등)의 모든 요소 중에서 조건에 맞는 요소만을 반환
'''
myList = [1, 2, 3, 4, 5]
myList2 = list(filter(lambda x : x % 2 ==1, myList))
print(myList2) 
## [1, 3, 5] 출력
'''
## sorted() : 시퀀스(리스트, 튜플 등)의 요소를 정렬한 결과를 반환
'''
myList = ['apple', 'bananaan', 'cherry']
myList2 = sorted(myList, key=lambda x: len(x))
print(myList2)
## 길이 순으로 정렬 해라 해서 ['apple', 'cherry', 'bananaan'] 출력
'''
## reduce() : 시퀀스(리스트, 튜플 등)의 모든 요소를 누적적으로 계산한 결과를 반환
'''
from functools import reduce
myList = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, myList)
print(result)
## 120 출력
'''
## 재귀함수
'''
def selfCall():
    print('하', end='')
    selfCall()
print(selfCall())
'''
## 입력한 숫자를 1까지 세는 함수를 재귀 함수로 작성
'''
def count(num):
    if num >= 1:
        print(num, end=" ")
        count(num-1)
    else:
        return
count(10)
print()
count(20)
'''
## 팩토리얼(Factorial)값을 구하는 함수 factorial(4) = 4*3*2*1
'''
def factorial(num):
    if num <= 1:
        return num
    else:
        return num * factorial(num-1)
print(factorial(4))
print(factorial(10))
'''
## 제너레이터와 yield
## yield 문 : 함수를 종결하지 않으면서 값을 계속 반환
## return 문은 값을 반환하고 종료됨
'''
def genFunc():
    yield 1
    yield 2
    yield 3

print(list(genFunc()))
'''
## 함수 내 yield가 있으면 생성자 함수라고 함.
## 생성자함수는 yield문으로 값을 반환한 후 계속 진행한다
## 제너레이터(Generator:생성자) 함수 : yield가 포함된 함수
## yield 문으로 값을 반환한 후 계속 진행
'''
def genFunc(num):
    for i in range(0, num):
        yield i
        print("제너레이터 진행 중")
for data in genFunc(5):
    print(data)
'''
