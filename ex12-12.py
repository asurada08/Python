import threading
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

## 메인 코드 부분
car1 = RacingCar("@자동차1")
car2 = RacingCar("#자동차2")
car3 = RacingCar("$자동차3")

th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()
'''
1행 : threading 모듈 임포트
21행 : threading.Thread(target = 메서드 또는 함수, args=(매개변수))형식 사용 스레드 생성
21행 : car1.runCar() 메서드명을 스레드로 생성
21~23행 : 스레드 3개 생성
25~27행 : 스레드 start()
'''
'''
파이썬은 스레드를 내부적으로 cpu 1개만 사용한다
그래서 동시에 수행해도 실제 속도는 느리다
반면 멀티 프로세스 기법은 동시에 cpu를 여러개 사용한다
'''