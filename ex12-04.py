## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2

    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
    
## 메인 코드 부분 ##
myCar1 = Car("빨강", 200)
myCar2 = Car("노랑", 180)

print("자동차1의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar2.color, myCar2.speed))
'''
6행 : 생성자에서 매개변수 2개를 받도록 설정
'''