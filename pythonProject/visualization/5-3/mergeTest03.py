import pandas as pd

mystorefile = 'store.csv'
mystore = pd.read_csv(mystorefile, encoding='utf-8', index_col=0, header=0)
print('\n매장 테이블')
print(mystore) 

districtfile = 'districtmini.csv'
district = pd.read_csv(districtfile, encoding='utf-8', header=0)
print('\n행정 구역 테이블')
print(district)

# 양쪽 모두 'sido', 'gungu' 컬럼이 존재합니다.
result = pd.merge(mystore, district, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)

print('\n머지된 결과')
print(result)

# _merge 컬럼이 "left_only"인 항목들을 조회합니다.
m_result = result.query('_merge == "left_only"')
print('\n좌측에만 있는 행')
print(m_result)

# 전처리에 필요한 군구 보정 파일
gungufile = open('../05.2 시각화 작업/gungufile.txt', encoding='utf-8')
gungu_lists = gungufile.readlines()

gungu_dict = {} # 군구 정보 사전
for onegu in gungu_lists :
    mydata = onegu.replace('\n', '').split(':')
    gungu_dict[ mydata[0] ] = mydata[1]

print('\n군구 사전의 내용')
print(gungu_dict)

# 람다 함수를 사용합니다.
mystore.gungu = mystore.gungu.apply( lambda data : gungu_dict.get(data, data))

print('\n수정된 가게 정보 출력')
print(mystore)