## 함수 선언 부분 ##
def func1():
    global a # global 예약어로 a 변수를 전역변수로 지정
    a = 10 # a 값을 10으로 변경 func1(), func2() 함수에서 모두 a 값 10으로 출력
    print("func1()에서 a 값 : %d" % a)

def func2():
    print("func2()에서 a 값 : %d" % a)

## 함수 변수 선언 부분 ##
a = 20

## 메인 코드 부분 ##
func1()
func2()
