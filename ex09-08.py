## 함수 선언 부분 ##
def func1():
    result = 100
    return result

def func2():
    print("반환값이 없는 함수 실행")

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = func1() # 반환값이 있는 함수인 func1()을 호출하면 func1()의 반환값을 hap에 넣음
print("func1()에서 돌려준 값 : %d" % hap)
func2() # 반환값이 없는 함수인 func2()를 호출하면 반환 하지 않음
