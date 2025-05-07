import folium, requests

address = '서울 마포구 신수동 451번지 세양청마루아파트 상가 101호'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

api_key = 'dce1afff29429463b1edc2ad5d8c5852'  #'인증키 입력'  이부분은 여러문에 인증키를 입력하여 실습하세요
header = {'Authorization': 'KakaoAK ' + api_key}

def getGoocoder(address):
    result = ""
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

address_latlng = getGoocoder(address)
latitude = address_latlng[0]
longitude = address_latlng[1]

print('주소지 :', address)
print('위도 :', latitude)
print('경도 :', longitude)

shopinfo = '교촌 신수점'
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='red', icon='info-sign')
folium.Marker([latitude, longitude], popup=shopinfo, icon=myicon).add_to(foli_map)

folium.CircleMarker([latitude, longitude], radius=300, color='blue',fill_color='red', fill=False, popup=shopinfo).add_to(foli_map)

foli_map.save('c:/imsi/my_map_graph.html')
print('파일 저장 완료')
