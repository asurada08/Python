from pandas import Series

myindex = ['용산구', '마포구', '영등포구', '서대문구', '광진구', '은평구', '서초구']
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)


print('\n색인의 이름으로 값 읽기')
print(myseries[['서대문구']])

print('\n라벨 이름으로 슬라이싱')
print(myseries['서대문구':'은평구'])

print('\n여러 개의 색인 이름으로 데이터 읽기')
print(myseries[['서대문구', '서초구']])

print('\n정수를 이용한 데이터 읽기')
print(myseries[[2]])

print('\n0, 2, 4번째 데이터 읽기')
print(myseries[0:5:2])

print('\n1, 3, 5번째 데이터 읽기')
print(myseries[[1, 3, 5]])

print('\n슬라이싱 사용하기')
print(myseries[3:6])

print('\n2번째 항목의 값 변경')
myseries[2] = 90

print('\n2번째 부터 4번째 까지 항목의 값 변경')
myseries[2:5] = 33

print('\n용산구와 서대문구만 55로 변경')
myseries[['용산구', '서대문구']] = 55

print('\n짝수 행만 80으로 변경')
myseries[0::2] = 80

print('\n시리즈 내용 확인')
print(myseries)
