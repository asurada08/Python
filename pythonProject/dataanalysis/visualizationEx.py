import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

theaterfile = 'theater.csv'
colnames = ['id', 'theater', 'region', 'bindo']
dftheater = pd.read_csv(theaterfile, names=colnames, header=None)
dftheater = dftheater.rename(index=dftheater.id)
dftheater = dftheater.reindex(columns=['theater', 'region', 'bindo'])
dftheater.index.name = 'id'
print('전체조회')
print(dftheater)

print('극장별 상영 횟수 집계')
mygrouping = dftheater.groupby('theater')['bindo']
sumSeries = mygrouping.sum()
meanSeries = mygrouping.mean()
sizeSeries = mygrouping.size()

print('Series 3개를 이용하여 DataFrame을 만들어 낸다')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1)
df.columns = ['함계', '평균', '개수']
print(df)
print('-' * 30)

mysize = len(mygrouping.groups)

df.plot(kind='barh', rot=0)
# df.plot(kind='barh', rot=0, alpha=0.7, legend=True, stacked=True)
plt.title(str(mysize) + '개 매장 집계 데이터')
# plt.show()
filename = 'visualizationEx_01.png'
plt.savefig(filename)

print('집계 메소드를 사전에 담아 전달하기')
print('지역의 개수와 상영 회수의 총합')
mydict = {'bindo': 'sum', 'region': 'size'}
result = dftheater.groupby('theater').agg(mydict)
print(result)
print('-' * 30)

print('넘파이를 이용한 출력')
result = mygrouping.agg([np.count_nonzero, 'mean', 'std'])
print(result)
print('-' * 30)


def myroot(values):
    # 총합에 root를 씌워서 반환해 주는 함수
    mysum = sum(values)
    return sqrt(mysum)


def plus_add(values, somevalue):
    # 총합에 root를 씌운 다음 somevalue를 더하여 반환해주는 함수
    # mysum = sum(values)
    # return sqrt(mysum) + somevalue

    # 이전 함수를 호출하는 방법
    result = myroot(values)
    return result + somevalue


mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용하기')
result = mygrouping.agg(myroot)
print(result)
print('-' * 30)

print('groopby와 사용자 정의 함수 (매개변수 2개) 사용하기')
result = mygrouping.agg(plus_add, somevalue=3)
print(result)
print('-' * 30)

print('칼럼 2개 이상을 그룹핑하기')
newgrooping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgrooping.count()
print(result)
print('-' * 30)

newDf = df.loc[:, ['평균', '개수']]
newDf.plot(kind='bar', rot=0)
plt.title('3개 극장의 평균과 상영관 수')
# plt.show()
filename = 'visualizationEx_02.png'
plt.savefig(filename)
print(filename + '파일이 저장되었습니다')

# labels : 원주 외각에 보여줄 라벨
labels = []
explode = (0, 0.03, 0.06)

for key in sumSeries.index:
    mydata = key + '(' + str(sumSeries[key]) + ')'
    labels.append(mydata)

fig1, ax1 = plt.subplots()
mytuple = tuple(labels)
ax1.pie(sumSeries, explode=explode, labels=mytuple, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')
# plt.show()
filename = 'visualizationEx_03.png'
plt.savefig(filename)
print(filename + '파일이 저장되었습니다')
