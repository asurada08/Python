## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed
    
## 변수 선언 부분 ##
car1, car2 = None, None

## 메인 코드 부분 ##
car1 = Car("페라리", 150)
car2 = Car("람보르기니", 120)

print("%s의 현재 속도는 %d 입니다" % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d 입니다" % (car2.getName(), car2.getSpeed()))