import numpy as np
import pandas as pd
from pandas import Series

filename = 'exce102.csv'

print('\n# 누락된 데이터가 있는 샘플 데이터 프레임')
myframe = pd.read_csv(filename, index_col='이름')
print(myframe)

print('\n# fillna() 메소드를 이용한 다른 값 대체하기')
# 누락된 값은 모드 0으로 치환하시오
print(myframe.fillna(0, inplace=False))

print('\n# inplacd=False이므로 원본은 변동 사항이 없다')
print(myframe)

# fillna() 메소드를 실행하면, 매번 새로운 객체로 반환한다
# 오리지널 기존 객체를 변경하려면 inplace=True 옵션을 사용하면 된다
# inplace=True 옵션 : 복사본을 생성하지 않고, 호출한 객체 자체를 변경하겠다(기본값 : False)
print('\n# inplace=True이므로 원본데이터가 변경된다')
myframe.fillna(0, inplace=True)
print(myframe)

print('\n# 누락된 데이터가 있는 샘플 데이터프레임')
myframe.loc[['강감찬', '홍길동'],['국어', '영어']] = np.nan
myframe.loc[['박영희', '김철수'],['수학']] = np.nan
print(myframe)

print('\n# 임의의 값을 다른 값으로 치환하기')
print('# "국어" 칼럼의 NaN 값들은 15로 변경하라')
mydict = {'국어': 15, '영어': 25, '수학': 35}
myframe.fillna(mydict, inplace=True)

print(myframe)

myframe.loc[['박영희'],['국어']] = np.nan
myframe.loc[['홍길동'],['영어']] = np.nan
myframe.loc[['김철수'],['수학']] = np.nan

print(myframe)

mydict = {'국어': myframe['국어'].mean(),
          '영어': myframe['영어'].mean(),
          '수학': myframe['수학'].mean()}

myframe.fillna(mydict, inplace=True)

print(myframe)
