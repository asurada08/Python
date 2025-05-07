import numpy as np
import pandas as pd
from pandas import DataFrame, Series

print('\n# 시리즈의 누락된 데이터 처리하기')
print('# 원본 시리즈')
myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)

print('\n# isnull() 함수는 값이 NaN이면 True를 반환합니다')
print('# 파이썬의 None도 NaN으로 취급됩니다')
print(myseries.isnull())

print('\n# notnull()인자를 이용하여 참인 학목들만 출력합니다')
print(myseries[myseries.notnull()])

print('\n# dropna() 함수는 누락된 데이터가 있는 행과 열을 제외시킨다')
print(myseries.dropna())

print('\n# 데이터프레임의 누락된 데이터 처리하기')
print('# 누락된 데이터가 있는 샘플 데이터프레임')
filename = 'exce102.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print(myframe)

print('\n# dropna() 인자는 NaN이 하나라도 있는 모든 행은 배제합니다.')
cleaned = myframe.dropna(axis=0)
print(cleaned)

print('\n# how="all" 옵션을 주면 모든 값이 NaN인 행만 배제합니다')
print('# 의미 있는 값이 하나라도 있으면 해당 행은 보여줍니다')
cleaned = myframe.dropna(axis=0, how='all')
print(cleaned)

print('\n# [영어]칼럼에 NaN이 있는 행들만 삭제하세요')
print(myframe.dropna(subset=['영어']))

print('\n#  칼럼을 배제하는 방법은 axis=1 옵션을 설정하면 된다')
# 나머지는 행을 배제할 때 옵션들과 동일하다
cleaned = myframe.dropna(axis=1, how='all')
print(cleaned)

print(myframe.dropna(axis=1, how='all'))

print('\n# thresh 옵션 사용하기')
print(myframe.dropna(axis=1, thresh=2))

print('\n# 열방향으로 NaN 값이 하나라도 존재하는 열은 모드 제거합니다')
print(myframe.dropna(axis=1, how='any'))
