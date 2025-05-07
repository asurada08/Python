import time

## 클래스 선언 부분 ##
class RacingCar:
    carName = ""
    def __init__(self, name):
        self.carName = name
    
    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + "~ 달립니다.\n"
            print(carStr, end="")
            time.sleep(0.1) # 0.1초 멈춤

## 메인 코드 부분 ##
car1 = RacingCar("@자동차1")
car2 = RacingCar("#자동차2")
car3 = RacingCar("$자동차3")

car1.runCar()
car2.runCar()
car3.runCar()
'''
4~13행 : RacingCar 클래스 정의
9~13행 : 자동차가 달린다는 것을 3번 출력하는 runCar() 메서드 만듬
13행 : 너무 빠른 출력 방지하려고 0.1초 동안 멈춤
20~22행 : 세 대가 차례로 출발
'''