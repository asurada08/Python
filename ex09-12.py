## 함수 선언 부분 ##
def para_func(*para): # *para로 매개변수 설정
    result = 0
    for num in para:
        result = result + num

    return result

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = para_func(10, 20) # 호출한 매개변수는 (10, 20) 형식의 튜플로 전달
print("매개변수가 2개인 함수를 호출한 결과 : %d" % hap)
hap = para_func(10, 20, 30) # 호출한 매개변수는 (10, 20, 30) 형식의 튜플로 전달
print("매개변수가 3개인 함수를 호출한 결과 : %d" % hap)
hap = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(hap)
