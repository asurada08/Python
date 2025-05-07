class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
    
    def downSpeed(self, value):
        self.speed -= value
        
def printMessage():
    print("시험 출력")

printMessage()
'''
5~6 행 : self, speed는 3행의 speed 의미, 자신의 클래스에 있는 speed 변수
11~12 행 : printMessage() 안에서는 필드를 사용하지 않으므로 이때는 self 생략가능
'''