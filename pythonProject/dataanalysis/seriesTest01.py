from pandas import Series

mylist = [10, 40, 30, 20]
myseries = Series(data=mylist, index=['강감찬', '이순신', '김유신', '광해군'])

print('\n# 자료형 확인')
print(type(myseries))

myseries.index.name = '점수'
print("\n#시리즈의 색인 이름")
print(myseries.index.name)

myseries.name = "학생들 시험"
print('\n#시리즈의 이름')
print(myseries.name)

print('#색인 확인하기')
print(myseries.index)

print('#시리즈의 값 확인')
print(myseries.values)

print('\n#시리즈 정보 출력')
print(myseries)

print('\n#반복하여 출력하기')
for idx in myseries.index:
    print('색인 : ' + idx + ', 값 : ' + str(myseries[idx]))