from pandas import Series

print('\n# 유일 값, 값 세기, 멤버십')
mylist = ['라일락', '코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(mylist)
print(myseries)

myunique = myseries.unique()
print(myunique)

# print(myseries.value_counts(normalize=True))
print(myseries.value_counts())

# '들장미', '라일락'이 들어있는 색인만 추출하겠습니다
# 데이터베이스의 in 절(clause)과 유사한 개념으로 봐도 무방합니다
mask = myseries.isin(['들장미', '라일락'])
print(mask)
print('-' * 30)

print(myseries[mask])
