from pandas.core.series import Series

sdata = [10, 40, 30, 20]
city = ['서울', '부산', '울산', '목포']
myseries2 = Series(data=sdata, index=city)

myseries2.name = '테스트'
myseries2.index.name = '지역'
print(myseries2)
