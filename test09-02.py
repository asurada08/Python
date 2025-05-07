## 사칙연산 계산하는 함수 작성 ##
## 함수 선언 부분 ##
def cals(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        try:
            if v1 == 0 or v2 == 0:
                result = v1 / v2
        except ZeroDivisionError:
            print("0으로는 나누면 안됩니다!")
        else:
            result = v1 / v2
    elif op == '**':
        result = v1 ** v2
    return result

## 전역 변수 선언 부분 ##
res = 0
val1, val2, oper = 0, 0, ""

## 메인 코드 부분 ##
val1 = int(input("첫번째 수를 입력하세요 : "))
oper = input("연산자를 입력하세요 : (+, -, *, /, **) :")
val2 = int(input("두번째 수를 입력하세요 : "))

res = cals(val1, val2, oper)

print("결과 : %d" % res)
