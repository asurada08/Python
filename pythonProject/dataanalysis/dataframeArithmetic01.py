import numpy as np
from pandas import Series, DataFrame

# 산술 연산과 데이터 정렬
myindex = ['강호민', '유재준', '신동진']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)
print('\n시리즈 출력 결과')
print(myseries)

myindex = ['강호민', '유재준', '이수진']
mycolumns = ['서울', '부산', '경주']
mylist = list(10 * onedata for onedata in range(1, 10))
# print(mylist)

myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns=mycolumns)
print('\n데이터프레임 출력 결과')
print(myframe)

# 데이터 프레임과 시리즈간에 산술연산이 가능하다
# axis=0이면 시리즈의 색인과 데이터 프레임의 색인간의 연산이 된다
# 양쪽에 공존하지 않으면 NaN


print('\nDataFrame + DataFrame')
result = myframe.add(myseries, axis=0)
print(result)

myindex2 = ['강호민', '유재준', '김병만']
mycolumns2 = ['서울', '부산', '대구']
mylist2 = list(5 * onedata for onedata in range(1, 10))
# print(mylist)

myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)), index=myindex2, columns=mycolumns2)
print('\n데이터프레임 출력 결과')
print(myframe2)

print('\nDataFrame + DataFrame')
result = myframe.add(myframe2, fill_value=0) # fill_value 기본값으로 사용할 값을 지정하는 역할
print(result)
