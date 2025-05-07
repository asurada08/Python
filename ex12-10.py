## 클래스 선언 부분 ##
class SuperClass:
    def method(self):
        pass

class SubClass(SuperClass):
    def method(self): # method 오버라이딩
        print("SubClass에서 method()를 오버라이딩함")
        
class SubClass2(SuperClass):
    pass

## 메인 코드 부분 ##
sub1 = SubClass()
sub2 = SubClass2()

sub1.method()
sub2.method()
'''
2~11행 : SuperClass 상속 받은 SubClass1, SubClass2 만듬
14~15행 : 각 인스턴스 sub1, sub2 생성
17~18행 : 오버라이딩한 method() 호출
raise NotImplementedError() 강제로 이벤트 발생
'''
