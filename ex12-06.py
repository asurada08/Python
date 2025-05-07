## 클래스 선언 부분 ##
class Car:
    color = "" # 인스턴스 변수
    speed = 0  # 인스턴스 변수
    count = 0  # 클래스 변수
    
    def __init__(self):
        self.speed = 0 # 클래스 인스턴스 변수 = 동적멤버변수
        Car.count += 1 # 정적멤버변수 = 클래스변수
        
## 변수 선언 부분 ##
myCar1, myCar2 = None, None

## 메인 코드 부분 ##
myCar1 = Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 chd %d대 입니다." % (myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 현재 속도는 %dkm, 생산된 자동차는 chd %d대 입니다." % (myCar2.speed, myCar2.count))
'''
5행 : 클래스 변수 count를 선언하고 0으로 초기화
7~9행 : 생성자 안에서 클래스 변수에 접근하려고 클래스명.count를 1 증가
'''