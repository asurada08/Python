import numpy as np
from pandas import DataFrame

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']
mycolumn = ['서울', '부산', '광주', '목포', '경주']
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist)

myframe = DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumn)
print(myframe)

print('\n# 1행만 시리즈로 읽어오기')
result = myframe.iloc[1]
print(type(result))
print(result)

print('\n# 몇개의 행을 읽어오기')
result = myframe.iloc[[1, 3]]
print(type(result))
print(result)

print('\n# 짝수 행만 가져오기')
result = myframe.iloc[0::2]
print(result)

print('\n# 이순신 행만 시리즈로 읽어오기')
result = myframe.loc['이순신']
print(type(result))
print(result)

print('\n# 이순신 행만 데이터프레임으로 읽어오기')
result = myframe.loc[['이순신']]
print(type(result))
print(result)

print('\n# 이순신과 강감찬 행 읽어오기')
result = myframe.loc[['이순신', '강감찬']]
print(type(result))
print(result)

print('>>>' * 30, '\n')

print(myframe.index)
print()

result = myframe.loc[['강감찬'], ['광주']]
print('1:', result, '\n')

result = myframe.loc[['연산군', '강감찬'], ['광주', '목포']]
print('2:', result, '\n')

result = myframe.loc['김유신':'광해군', '광주':'목포']
print('3:', result, '\n')

result = myframe.loc['김유신':'광해군', ['부산']]
print('4:', result, '\n')

result = myframe.loc[[False, True, True, False, True]]
print('5:', result, '\n')

result = myframe.loc[myframe['부산'] <= 100]
print('6:', result, '\n')

result = myframe.loc[myframe['목포'] == 140]
print('7:', result, '\n')

cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140

print(type(cond1))  # bool 값 출력
print(cond1)
print('-' * 40)

print(type(cond1))  # bool 값 출력
print(cond2)
print('-' * 40)

df = DataFrame([cond1, cond2])
print('8:', df, '\n')
print('-' * 40)

print('9:', df.all(), '\n')
print('-' * 40)

print('10:', df.any(), '\n')
print('-' * 40)

result = myframe.loc[df.all()]
print('11:', result, '\n')
print('-' * 40)

result = myframe.loc[df.any()]
print('12:', result, '\n')
print('-' * 40)

print('\n람다 함수의 사용')
result = myframe.loc[lambda df: df['광주'] >= 130]
print(result)

print('\n# 이순신과 강감찬의 부산 실적을 30으로 변경하기')
myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(myframe)

print('\n# 김유신부터 광해군까지 경주 실적을 80으로 변경하시오')
myframe.loc['김유신':'광해군', ['경주']] = 80
print(myframe)

print('\n# 연산군의 모든 실적을 50으로 변경하기')
myframe.loc[['연산군'], :] = 50
print(myframe)

print('\n# 모든 사람의 광주 컬럼을 60으로 변경하기')
myframe.loc[:, ['광주']] = 60
print(myframe)

print('\n# 경주 실적이 60 이하인 데이터를 모두 0으로 변경하기')
myframe.loc[myframe['경주'] <= 60, ['경주', '광주']] = 0
print(myframe)
