## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        if value > 150:
            value = 150
        elif value <0:
            value = 0
        self.speed += value
        
    
    def downSpeed(self, value):
        if value > 150:
            value = 150
        elif value <0:
            value = 0
        self.speed -= value

## 메인 코드 부분
myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "yellow"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "black"
myCar3.speed = 0

myCar1.upSpeed(180)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(80)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(-10)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))