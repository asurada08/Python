from pandas import DataFrame

sdata = {
    '도시': ['서울', '서울', '서울', '부산', '부산'],
    '연도': [2000, 2001, 2002, 2001, 2002],
    '실적': [150, 170, 360, 240, 240]
}

# 색인을 지정하지 않으면 0부터는 일련번호가 자동으로 설정된다
# myFrame = DataFrame(sdata)

myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex)
# print(myframe)

print('\n타입 확인 :', type(myframe))

myframe.columns.name = '칼럼1'
print('\n칼럼 정보 확인 ')
print(myframe.columns)

myframe.index.name = '색인1'
print('\n색인 정보 확인 ')
print(myframe.index)

print('\n들어있는 내용 확인 ')
print(type(myframe.values))  # ndarray
print(myframe.values)

print('\n자료형 확인 ')
print(myframe.dtypes)

print('\n내용 확인 ')
print(myframe)

print('\n행과 열을 전치 시킵니다. ')
print(myframe.T)

print('\ncolums 속성 사용해보기 ')
mycolums = ['실적', '도시', '연도']
newframe = DataFrame(sdata, columns=mycolums)
print(newframe)
