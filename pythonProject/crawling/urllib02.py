import urllib.request  # 라이브러리 읽어 들이기

# URL과 저장 경로 지정하기
url = 'http://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg'
savename = 'urldownload02.png'

# urlopen() 함수를 사용하면 네트워크를 통해 원격 객체를 읽고 메모리에 올리는 역할을 수행
# urlopen() 함수를 이용하여 다운로드한다
result = urllib.request.urlopen(url)

# read() 함수를 이용하여 바이너리 형식으로 변경해준다
data = result.read()
print('# type(data) :', type(data))

# 파일로 저장하기
with open(savename, mode='wb') as f:
    f.write(data)
    print(savename + ' 파일로 저장되었습니다')
