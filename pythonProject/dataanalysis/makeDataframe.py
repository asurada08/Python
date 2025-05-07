import numpy as np
from pandas import DataFrame

mydata = np.arange(9).reshape((3, 3))  # reshape() 자리 튜플, 리스트 둘다 가능
myframe = DataFrame(data=mydata, index=['용산구', '마포구', '은평구'], columns=['김철수', '이영희', '정준수'])
print(myframe)

sdata = {'지역': ['용산구', '마포구'], '연도': [2019, 2020]}
myframe = DataFrame(data=sdata)
print(myframe)

sdata = {'용산구': {2020: 10, 2021: 10}, '마포구': {2020: 30, 2021: 40, 2022: 50}}
myframe = DataFrame(sdata)
print(myframe)

sdata = {'지역': ['용산구', '용산구', '용산구', '마포구', '마포구'], '연도': [2019, 2020, 2021, 2020, 2021], '실적': [20, 30, 35, 25, 45]}
myframe = DataFrame(sdata)
print(myframe)
