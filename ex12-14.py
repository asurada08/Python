## 연산자 오버로딩
## 산술
'''
class My:
    def __init__(self, i):
        self.i = i
        
    def __str__(self, i):
        return str(self, i)
    
    def __add__(self, value):
        return self.i + value
    
    def __radd__(self, value):
        return self.i + value
    
    def __sub__(self, value):
        return self.i - value
    
    def __mul__(self, value):
        return self.i * value
    
    def __truediv__(self, value): # 2.x : __div__ 3.x : __truediv__
        return self.i / value
    
i = My(20)
print(i+10); print(10+i); print(i-10); print(i*10); print(i/10); print("큰"+"글자")
'''
## 비교
'''
class Comp:
    def __init__(self, i):
        self.i = i
    
    def __gt__(self, y):
        return self.i > y
        
    def __ge__(self, y):
        return self.i >= y
        
    def __lt__(self, y):
        return self.i < y
        
    def __le__(self, y):
        return self.i <= y
        
    def __eg__(self, y):
        return self.i == y
        
    def __ne__(self, y):
        return self.i != y

c = Comp(10)
print(c > 1);print(c >= 1);print(c < 1);print(c <= 1);print(c == 1);print(c != 1)
'''
## 시퀀스 / 매핑 오버로딩
'''
class SeqClass:
    def __init__(self, i):
        self.i = i
    
    def __len__(self): # len(객체)
        return self.i

s1 = SeqClass(10)
print(len(s1)) # 시퀀스(연속적인 값)
# TypeError: SeqClass.__init__() missing 1 required positional argument: 'i'
# s2 = 10
# print(len(s2)) #시퀀스야 되는데 정수여서 에러 발생
# TypeError: object of type 'int' has no len()
'''
## 시퀀스 / 매핑 오버로딩(2)
'''
class SeqClass:
    def __init__(self, i):
        self.i = i
    
    def __getitem__(self, k): # 키, 값 
        if k < 0 or self.i <= k:
            raise IndexError("Out of Index - "+str(k)) # 강제 except 발생시킴
        return k*k

s1=SeqClass(10)
print(s1[0]); print(s1[1]); print(s1[4]); print(s1[9]); print(list(s1)); print(tuple(s1))
# print(s1[11]) IndexError: Out of Index - 11
'''
## 오버라이딩
'''
class Person:
    def __init__(self, name, phone = None): # 생성자
        self.name = name
        self.phone = phone

    def __str__(self): # 문자열 오버로딩
        return "<person {0} {1}>".format(self.name, self.phone)
    
class Employee(Person):
    def __init__(self, name, phone, position, salary): # 생성자
        Person.__init__(self, name, phone) # 부모생성자 호출
        self.position = position
        self.salary = salary
        
    def __str__(self): # 문자열 오버로딩 / 오버라이딩
        return "<person {0} {1} {2} {3}>".format(self.name, self.phone, self.position, self.salary)

p1 = Person("제임스", 1498)
print(p1.name); print(p1); print()

m1 = Employee("리차드", 5564, "대리", 1989)
print(m1.name, m1.position); print(m1)
'''
## 오버라이딩2
'''
class Animal:
    def cry(self):
        return "으앙으앙"
    
class Dog(Animal):
    def cry(self, a, b):
        return a*b

class Duck(Animal):
    def cry(self, a, b):
        return a+b
    
class Cat(Animal):
    pass

a = Dog(); b = Duck(); c = Cat()
print(a.cry("멍멍 ",3)); print(b.cry("꽥꽥 ","꽥꽥")); print(c.cry())

## 상속관계 알아내기
# isinstance(객체, 클래스) -- bool
# issubclass(클래스, 클래스) -- bool
print(isinstance(a, Duck))
print(issubclass(Duck, Cat))
print(issubclass(Dog, Animal))
'''
## 정적 메소드 : @staticmethod 붙이고 (self) X
'''
class A:
    def per(slef, x, y): #instance method, 사용하려면 반드시 객체.메소드()
        print("instance method", x, y)
        
c = A()
c.per(1, 2) # 객체.method (O)
# A.per(1, 2) # class.method 라서 오류
#TypeError: A.per() missing 1 required positional argument: 'y'
'''
'''
class A:
    @staticmethod
    def per(x, y): 
        print("instance method", x, y)
        
c = A()
c.per(1, 2) # 객체.method 
A.per(10, 20) # class.method
'''
## 소멸자
'''
class A:
    def __init__(self):
        self.name = "A"
        print("클래스가 생성 되었습니다", self.name)
        
    @staticmethod
    def per(x, y): 
        print("instance method", x, y)
    
    def __del__(self): # 소멸자
        print("클래스가 소멸 되었습니다")
        
c = A()
c.per(1, 2) # 객체.method 
A.per(10, 20) # class.method

d = A()
'''