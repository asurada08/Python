## 클래스
'''
클래스 모양과 생성 
calss 클래스명:
    # 관련코드 구현 부분
'''
## 클래스 사용순서
'''
1단계 : 클래스 선언 / class 클래스명:
2단계 : 인스턴스 생성 / 인스턴스 = 클래스명()
3단계 : 필드나 메서드 사용 / 인스턴스.필드명 = 값, 인스턴스.메서드()
'''
## 생성자 : 인스턴스를 생성하면서 필드값을 초기화 시키는 함수
## 생성자의 기본형태 : __init__()
'''
class Car:
    color = ""
    speed = 0
    
    def __init__(self):
        self.color = "red"
        self.speed = 0
'''
## 인스턴스 변수
'''
ex) Car 클래스 2개의 필드
class Car:
    color = "" # 필드 : 인스턴스 변수
    speed = 0  # 필드 : 인스턴스 변수
ex) 클래스를 이용해 메인 코드에서 인스턴스 만들기
myCar1 = Car()
myCar2 = Car()
'''
## 클래스 변수 : 클래스 안에 공간이 할당된 변수, 여러 인스턴스가 클래스 변수 공간 함께 사용
'''
class Car:
    color = ""
    speed = 0
    count = 0

myCar1 = Car()
myCar2 = Car()
count 공유함.
'''
## 상속의 개념 : 기존 클래스에 있는 필드와 메서드를 그대로 물려받는 새로운 클래스를 만드는것
## 공통된 내용을 자동차 클래스에 두고 상속을 받음으로써 일관되고 효율적인 프로그래밍 가능
## 상위 클래스인 자동차 클래스를 슈퍼클래스, 부모클래스, 하위의 승용차, 트럭 클래스는 서브클래스, 자식클래스라 함
## 상속 구현 문법 : class 서브클래스(슈퍼클래스):

## 메서드 오버라이딩 : 상위 클래스의 메서드를 서브클래스에서 재정의
## super()함수 : 서브클래스에서 메서드 오버라이딩을 할 때, 
## 슈퍼클래스의 메서드나 속성을 사용해야 하는경우엔 super()메서드를 사용하면 된다
'''
class Car:
    value = "슈퍼 값"
    def carMethod(self):
        print("슈퍼클래스 메서드 실행~")
class sedan(Car):
    value = "서브 값"
    def carMethod(self):
        super().carMethod() # Car 클래스의 carMethod()가 실행
        print("서브 클래스 메서드 실행~")
        print(super().value) # Car 클래스의 value가 출력됨
'''
## super() 관련 보충
'''
super() 생성자 : 호출 X
super().메서드명() : 호출 O
super().필드명() : 호출 X
this(X), self(O)
'''
## 클래스의 특별한 메서드
'''
__del__() 메서드 : 소멸자(Destructor), 생성자와 반대로 인스턴스 삭제할 때 자동 호출
__repr__() 메서드 : 인스턴스를 print() 문으로 출력할 때 실행
__add__() 메서드 : 인스턴스 사이에 덧셈 작업이 일어날 때 실행되는 메서드, 인스턴스 사이의 덧셈 작업 가능
비교 메서드 : __lt__(), __le__(), __gt__(), __ge__(), __eq()__, __ne__()
             (<,<=,>,>=,==,!= 등) 사용할 때 호출
'''
'''
연산자 오버로딩
1. 수치 연산자 오버로딩:
__add__(self, value)  --> +  
__sub__(self, value)  --> -
__mul__(self, value)  --> *
__truediv__(self, value)  --> /
예)  변수i= 클래스(10)
     print(i+10)--> 20
     print(10 + i)--> 오류남, 
     값+객체가 나오면 __radd__(self, value)--> 연산자 앞에 r을 붙여야 함

2. 비교연산자
__lt__(self,value)  self < value
__le__(self,value)  self <= value
__eq__(self,value)  self == value
__ne__(self,value)  self != value
__gt__(self,value)  self > value
__ge__(self,value)  self >= value

3. 시퀀스/매핑 자료형 연산자 오버로딩
메소드                          연산자
__len__(self)                ---> len()
__contains__(self,item)      ----> item in self
__getitem__(self,key)        ----> self[key]
__setitem__(self,key, value) --> self[key]=value
__delitem__(self,key)        --> del self(k)
'''
'''
class My:
    def __init__(self, i):
        self.i = i
    def __radd__(self, other):
        return self.i+other
i=My(10)
#print(i+10) # 객체 + 값 나오면 __add__
print(10+i) # 값 + 객체 나오면 __radd__
'''
## 추상 메서드 : 서브 클래스에서 메서드를 오버라이딩,
## 슈퍼클래스에서는 빈 껍질의 메서드만 만들어 놓고 내용은 pass로 채움

## 멀티 스레드 : 프로그램 하나에서 여러 개를 동시에 처리할 수 있도록 제공하는 기능
'''
일반 프로그램 : -작업1->-작업2->-작업3->
스레드        : -작업1->
                -----작업2----->
                       -----작업3----->

'''