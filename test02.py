import math

a = int(input("첫번째 정수 : "))
b = int(input("두번째 정수 : "))

print("첫번째 정수 : %d" % a)
print("두번째 정수 : %d" % b)

result = a + b
print(a, "+", b, "=", result)
print("%d + %d = %d" %(a, b, result))
print("{0} + {1} = {2}".format(a, b, result))
print("{su1} + {su2} = {su3}".format(su1=a,su2=b,su3=result))

'''
print("{위치:채울문자 정렬방식 자릿수}".format("출력할문자"))
       {0: <왼쪽정렬, >오른쪽정렬, ^가운데정렬, 채울문자 생략하면 공백}
'''

result = a * b
print(a, "*", b, "=", result)
print("%d * %d = %d" %(a, b, result))
print("{0} * {1} = {2}".format(a, b, result))
print("{su1} * {su2} = {su3}".format(su1=a, su2=b, su3=result))

result = math.pow(a, b)
print("pow사용,", a, "^", b, "=", result)
print("pow사용, %d ^ %d = %d" %(a, b, result))
print("pow사용, {0} ^ {1} = {2}".format(a, b, result))
print("pow사용, {su1} ^ {su2} = {su3}".format(su1=a, su2=b, su3=result))

result = a ** b
print("제곱하면,", a, "^", b, "=", result)
print("제곱하면, %d ^ %d = %d" %(a, b, result))
print("제곱하면, {0} ^ {1} = {2}".format(a, b, result))
print("제곱하면, {su1} ^ {su2} = {su3}".format(su1=a, su2=b, su3=result))
