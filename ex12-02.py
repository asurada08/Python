## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
    
    def downSpeed(self, value):
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

myCar1.upSpeed(100)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(80)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(60)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))
'''
2~10행 : Car 클래스 정의
3~4행 : 자동차의 색상 속도 필드 정의
6~10행 : 매개변수로 추가속도(value)를 받아 현재속도(self, speed) 증가 또는 감소
13~23행 : myCar1, myCar2, myCar3 인스턴스를 생성하고, 색상과 속도 지정
25행 : myCar1의 upSpeed(100) 메서드 호출하면 myCar1의 필드 중 speed 필드가 100으로 증가
25~ 32행 : color, speed 필드 출력
'''