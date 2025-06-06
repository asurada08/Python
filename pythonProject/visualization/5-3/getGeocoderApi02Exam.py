import folium
import requests
import pandas as pd

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='
api_key = 'dce1afff29429463b1edc2ad5d8c5852'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGeoCoder(address):
    result = ""
    url = url_header + address
    r = requests.get(url, headers=header)
    # print(r)
    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

def makeMap(brand, store, geoInfo):
    # 브랜드 이름(brand), 상호명(store), 위도 경도 튜플(geoInfo)
    shopinfo = store + '(' + brand_dict[brand] + ')' # 가게이름(브랜드)
    mycolor = brand_color[brand]
    latitude, longitude = float(geoInfo[0]), float(geoInfo[1])
    # print(longitude, geoInfo[1], shopinfo)

    marker = folium.Marker([latitude, longitude], popup=shopinfo, \
              icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)

# 지도의 기준점
# mylatitude = 32.00
mylatitude = 33.40
mylongitude = 126.60
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=11)

brand_dict = {'cheogajip':'처가집', 'goobne':'굽네', 'kyochon':'교촌', 'pelicana':'페리카나', 'nene':'네네'}
brand_color = {'cheogajip':'red', 'goobne':'green', 'kyochon':'pink', 'pelicana':'yellow', 'nene':'blue'}

csv_flle = 'allStoreModified.csv'
myframe = pd.read_csv(csv_flle, index_col=0, encoding='utf-8')

sido = "제주특별자치도"
condition1 = myframe['sido'] == sido
mapData = myframe.loc[condition1]

ok = 0
notok = 0
for idx in range(len(mapData.index)):
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    geoInfo = getGeoCoder(address)

    if geoInfo == None:
        print('낫오케이 : ' + address)
        notok += 1
    else :
        # print(geoInfo)
        print('오케이 : ' + brand + ' ' + address)
        ok += 1
        makeMap(brand, store, geoInfo)
    print('%'*30)
# end for

total = ok + notok
print('ok :', ok)
print('notok :', notok)
print('total :', total)

filename = 'c:/imsi/mapresult.html'
mapObject.save(filename)

print('파일 저장 완료')
