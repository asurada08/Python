## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self):
        self.color = "red"
        self.speed = 0
        
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

## 메인 코드 부분 ##
myCar1 = Car()
myCar2 = Car()

print("자동차1의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar2.color, myCar2.speed))
'''
기본생성자 : 매개변수가 self만 있는 생성자
코드양을 줄이려고 myCar1, myCar2만 사용
6~8행 : 생성자가 25~26행에서 자동으로 값 초기화
'''