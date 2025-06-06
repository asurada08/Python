import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

filename = '점수데이터.csv'
myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print(myframe['jumsu'].unique())

frame01 = myframe.loc[myframe['jumsu'] == 'lower', 'length']
frame01.index.name = 'lower'
print(frame01.head())

frame02 = myframe.loc[myframe['jumsu'] == 'upper', 'length']
frame02.index.name = 'upper'
print(frame02.head())

# axis=0 : 행을 따라 연산, axis=1 열을 따라 연산
# axes : 그래프의 좌표를 나타낼때(x, y)
totalframe = pd.concat([frame01, frame02], axis=1, ignore_index=True)
totalframe.columns = ['lower', 'upper']
print(totalframe.head())

totalframe.plot(kind='box')

plt.xlabel('점수 구분')
plt.ylabel('길이')
plt.grid(False)
plt.title('점수에 따른 길이의 상자 수염 그래프')

filename = 'boxPlot01_image.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다')
plt.show()
