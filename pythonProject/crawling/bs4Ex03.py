import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'http://move.naver.com/movie/sdb/rank/rmove.naver'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class': 'tit3'})
print('-' * 30)
print(tags)
print('-' * 30)

print(r'\n영화 제목만 뽑아내기')
for tag in tags:
    # 하위 <a> 태그 아래의 글자 영역
    print(tag.a.string)  # text 속성도 동일한 결과를 보여 준다

print(r'\n앵커의 href 속성')
url_header = 'http://move.naver.com'
for tag in tags:
    print('-' * 50)
    print(url_header + tag.a['href'])

mytrs = soup.find_all('tr')

no = 0
totallist = []

for one_tr in mytrs:
    title = ''
    up_down = ''
    mytd = one_tr.find('td', attrs={'class': 'title'})
    if mytd != None:
        no += 1
        newno = str(no).zfill(2)

        mytag = mytd.find('div', attrs={'class': 'tit3'})
        title = mytag.a.string

        mytd = one_tr.select_one('td:nth-of-type(3)')
        myimg = mytd.find('img')
        if myimg.attrs['alt'] == 'up':
            up_down = '상승'
        elif myimg.attrs['alt'] == 'down':
            up_down = '강등'
        else:
            up_down = '불변'

        change = one_tr.find('td', attrs={'class': 'range ac'})
        if change == None:
            pass
        else:
            change =change.string
            # print(newno + '/' + title + '/'+ up_down + '/' + change)
            totallist.append((newno, title, up_down, change))

mycolumn = ['순위', '제목', '변동', '변동값']

myframe = DataFrame(totallist, columns=mycolumn)
filename = 'naverMovie.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print(filename, '으로 저장 되었습니다.', sep='')

