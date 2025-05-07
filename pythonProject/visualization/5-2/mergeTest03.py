import pandas as pd

mystorefile='store.csv'
mystore=pd.read_csv(mystorefile,encoding='utf-8',index_col=0,header=0)
print('매장 테이블')
print(mystore)

districtfile='districtmini.csv'
district=pd.read_csv(districtfile,encoding='utf-8',header=0)
print('행정 구역 테이블')
print(district)

result=pd.merge(mystore,district,on=['sido','gungu'],how='outer',suffixes=['','_'],indicator=True)

print('\n머지된 결과')
print(result)

m_result=result.query('_merge == "left_only"')
print('\n좌측에만 있는 행')
print(m_result)

gungufile=open('gungufile.txt',encoding='utf-8')
gungu_lists=gungufile.readlines()

gungu_dict={}
for onegu in gungu_lists:
    mydata=onegu.replace('\n', '').split(':')
    gungu_dict[mydata[0]]=mydata[1]

print('\n군구 사전의 내용')
print(gungu_dict)

mystore.gungu=mystore.gungu.apply(lambda data:gungu_dict.get(data,data))

print('\n 수정된 가게 정보 출력')
print(mystore)