import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
filename = '프로야구타자순위2021년.csv'

myframe = pd.read_csv(filename, encoding='utf-8')
print('head() 메소드 실행 결과')
print(myframe.tail(10))

print(myframe.info())  # 데이터가 데이터프레임이라 알려주고, 색인의 유형, 컬럼의 정보 출력

mycolors = ['r', 'g', 'b']
labels = ['롯데', 'NC', 'KT']
print(labels)

cnt = 0  # 카운터 변수

# 색상은 '팀명'으로 구분하도록 합니다
for finditem in labels:
    xdata = myframe.loc[myframe['팀명'] == finditem, '안타']
    ydata = myframe.loc[myframe['팀명'] == finditem, '타점']
    plt.plot(xdata, ydata, color=mycolors[cnt], marker='o', linestyle='None', label=finditem)
    cnt += 1

plt.legend(loc=4)  # 숫자 4는 오른쪽 하단에 범례를 위치시킵니다
plt.xlabel('안타 개수')
plt.ylabel('타점')
plt.title('안타와 타점에 대한 산점도')
plt.grid(True)

plt.show()
