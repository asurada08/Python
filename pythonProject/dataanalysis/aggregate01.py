import numpy as np
from pandas import DataFrame

mydata = [[10.0, np.nan, 20.0], [20.0, 30.0, 40.0],
          [np.nan, np.nan, np.nan], [40.0, 50.0, 30.0]]
myindex = ['이순신', '김유신', '윤봉길', '계백']
mycolumn = ['국어', '영어', '수학']
myframe = DataFrame(data=mydata, index=myindex, columns=mycolumn)
print('\n# 성적 데이터프레임 출력')
print(myframe)

print('\n# 집계 함수는 기본값으로 누락도니 데이터(NaN)을 배제하고 연산합니다')
# sum() 메소드를 호출하면 각 컬럼의 합을 담은, 시리즈를 반환합니다
print('\n# sum 함수 사용시 (axis=0)은 열 방향으로 합산합니다')
print(myframe.sum(axis=0))

print('\n# sum 함수 사용 시 (axis=1)은 행 방향으로 합산합니다')
print(myframe.sum(axis=1))

print('\n# mean, axis=1, skipna=False 옵션 사용하기')
print(myframe.mean(axis=1, skipna=False))

# 행 또는 열에 1개 이상의 NaN이 존재 할 때,
# 이 행 또는 열을 무시하려면 skipna=True 옵션을 사용합니다
print('\n# mean, axis=1, skipna=True 옵션 사용하기')
print(myframe.mean(axis=1, skipna=True))

print('\n# max, axis=1, skipna=False 옵션 사용하기')
print(myframe.max(axis=1, skipna=False))

print('\n# max, axis=1, skipna=True 옵션 사용하기')
print(myframe.max(axis=1, skipna=True))

print('\n# idxmax() 메소드 : 최댓값을 가지고 있는 색인을 반환합니다')
print(myframe.idxmax())

print("\n# 원본 데이터프레임")
print(myframe)

print('\n# 누적 합 메소드 : 누적 합 구하기(axis=0)')
print(myframe.cumsum(axis=0))

print('\n# 누적 합 메소드 : 누적 합 구하기(axis=1)')
print(myframe.cumsum(axis=1))

print('\n# 평균 구하기')
print(myframe.mean())

# NaN이 아닌 값들의 평균값으로 대체하는 예시
# NaN 값에 대한 처리
# myframe.loc[myframe['국어'].isnull(), '국어'] = 55
# myframe.loc[myframe['영어'].isnull(), '영어'] = 60
# myframe.loc[myframe['수학'].isnull(), '수학'] = 30

# 평균 값으로 대체하는 경우
print('\n# NaN값 평균값으로 대체')
myframe.loc[myframe['국어'].isnull(), '국어'] = myframe['국어'].mean()
myframe.loc[myframe['영어'].isnull(), '영어'] = myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(), '수학'] = myframe['수학'].mean()
print(myframe)

print('\n# describe() 메소드는 시리즈에도 사용이 가능합니다')
print('# describe() 메소드 : 1번에 통계 결과를 여러 개 만들어 낼 때 사용합니다')
print(myframe.describe())

print(myframe)
