import threading

## 클래스 선언 부분 ##
class cal:
    calVal = 0
    def __init__(self, value):
        self.calVal = value
    
    def calHap(self):
        hap = 0
        for i in range(1, self.calVal + 1):
            hap += i
        print("1부터 %d 까지 합 = %d" % (self.calVal, hap))  # 결과 출력

## 메인 코드 부분 ##
val1 = cal(10000)
val2 = cal(100000)
val3 = cal(1000000)

th1 = threading.Thread(target=val1.calHap)
th2 = threading.Thread(target=val2.calHap)
th3 = threading.Thread(target=val3.calHap)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()
