from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "http://comic.naver.com/webtoon/weekday.naver"

# 이 페이지에 request해서 데이터를 가져온 후 변수에 저장한다
response = urlopen(myurl)

# <class 'http.client.HTTPResponse'>
print(type(response))
print('-' * 30)

# BeautifulSoup()를 이용해서 데이터를 분석한다
soup = BeautifulSoup(response, 'html.parser')

# Beautiful Soup 객체를 적절한 들여쓰기 형태로 출력해준다
print(soup.prettify())
print('-' * 30)

title = soup.find("title").string
print(title)
print('-' * 30)
