import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'

csv_flle = 'allStoreModified.csv'
myframe = pd.read_csv(csv_flle, index_col=0, encoding='utf-8')
# print(myframe.info())

print(myframe['brand'].unique())

mycolor = ['r', 'g', 'b', 'm']
brand_dict = {'cheogajip':'처가집', 'goobne':'굽네', 'kyochon':'교촌', 'pelicana':'페리카나', 'nene':'네네'}

seoulframe = myframe.loc[myframe['sido'] == '서울특별시']
kkframe = myframe.loc[myframe['sido'] == '경기도']

# '서울특별시', '경기도'를 합친 데이터
newframe = pd.concat([seoulframe, kkframe], axis=0)
print(newframe)

mygrouping=newframe.groupby(['brand'])['brand']
chartData=mygrouping.count()
chartData.index = [brand_dict[item] for item in chartData.index]
print(chartData)
plt.figure()
chartData.plot(kind='bar', rot=0, title='서울/경기도 점포 개수', legend=False, color=mycolor)
filename= 'makeChickenGraph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' 파일이 저장되었습니다.')
