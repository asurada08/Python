import urllib.request  # 라이브러리 읽어 들이기

# URL과 저장 경로 지정하기
url = 'http://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg'
savename = 'urldownload01.png'

# urlretrieve() 함수는 url 주소의 파일을 다운로드함
urllib.request.urlretrieve(url, savename)

print('웹에 있는 이미지 ' + url + '를 ', end='')
print(savename + ' 파일로 저장하였습니다')
