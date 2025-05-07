## 클래스 선언 부분 ##
class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("현재 속도(슈퍼클래스) : %d" % self.speed)
        
class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150:
            self.speed = 150
            
            print("현재 속도(서브클래스) : %d" % self.speed)

class Truck(Car):
    pass

## 변수 선언 부분 ##
sedan1, truck1 = None, None

## 메인 코드 부분 ##
truck1 = Truck()
sedan1 = Sedan()

print("트럭 : ", end = "")
truck1.upSpeed(200)

print("승용차 : ", end = "")
sedan1.upSpeed(200)

'''
9~15행 : 서브 클래스(Sedan)의 upSpeed() 메서드 다시 만듬
31행 : Sedan 인스턴스의 upSpeed() 메서드 호출하면 9행에서 재 정의된 upSpeed() 메서드 호출
17행 : 서브 클래스(Truck)에는 아무런 내용 없어 슈퍼클래스(Car)의 메서드를 그대로 상속
28행 : Truck 인스턴스의 upSpeed() 호출하면 3~6행 슈퍼클래스(Car)의 upSpeed() 메서드 호출
'''