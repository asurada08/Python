import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
# 엑셀 파일을 읽어와서 막대 그래프를 그려준다
# row 1개를 그룹으로 묶어 차트를 그려준다
filename = 'ex802.csv'

myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(city)'

myframe.plot(kind='bar', rot=0, title='지역별 차량 등록 대수', legend=True)
# plt.legend(loc=4) # 범례의 위치 : 오른쪽 하단(숫자 4)

print(myframe)

filename = 'dataframeGraph02_01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다')

myframeT = myframe.T
print(myframeT)
print('-' * 40)

myframeT.plot(kind='bar', rot=0, title='지역별 차량 등록 대수', legend=True)
filename = 'dataframeGraph02_02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다')

ymax = myframeT.sum(axis=1)
ymaxlimit = ymax.max() + 10

myframeT.plot(kind='bar', ylim=[0, ymaxlimit], rot=0, stacked=True,
              title='지역별 차량 등록 대수', legend=True)
filename = 'dataframeGraph02_03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다')
