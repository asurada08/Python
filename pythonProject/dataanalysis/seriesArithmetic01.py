from pandas import Series, DataFrame

# 시리즈의 산술 연산
myindex1 = ['강호민', '유재준', '김제명', '신동진']
mylist1 = [30, 40, 50, 60]

myindex2 = ['강호민', '유재준', '김제명', '이수진']
mylist2 = [20, 40, 60, 70]

myseries1 = Series(data=mylist1, index=myindex1)
myseries2 = Series(data=mylist2, index=myindex2)

print('\n# 시리즈 1 데이터')
print(myseries1)

print('\n# 시리즈 2 데이터')
print(myseries2)

# 산술연산
print(myseries1 + 5) # add
print('-' * 50)

print(myseries1.add(5))
print('-' * 50)

print((myseries1 - 10)) # sub
print('-' * 50)

print(myseries1 * 2) # mul
print('-' * 50)

print(myseries1 / 3) # div, floordiv
print('-' * 50)

# 관계연산
print(myseries1 >= 40)
print('-' * 50)

print('\n# 두 시리즈 더하기(한쪽에만 있는 데이터는 NaN으로 처리됨')
newseries = myseries1 + myseries2
print(newseries)

print('\n# 두 시리즈 빼기(fill_value에 의하여 0으로 처리된 후 연산 수행됨')
newseries = myseries1.sub(myseries2, fill_value = 0)
print(newseries)
