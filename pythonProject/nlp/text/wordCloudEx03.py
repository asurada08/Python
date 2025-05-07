import nltk
import matplotlib.pyplot as plt
import numpy as np

from wordcloud import WordCloud
from PIL import Image
from konlpy.tag import Komoran
from wordcloud import ImageColorGenerator

filename = '애국가(가사).txt'
ko_con_text = open(filename, encoding='utf-8')
ko_con_text = ko_con_text.read()

print('\ntype(ko_con_text)')
print(type(ko_con_text))  # str

print('\n애국가 4절까지의 문자열')
print(ko_con_text)  #

komo = Komoran()

tokens_ko = komo.nouns(ko_con_text)
print('\n형태소 분석된 각 단어들 출력')
print(tokens_ko)

stop_words = ['제', '월', '일', '조', '그', '아', '절', '위']  # 불용어

tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]
print('\nstop_words에 불용어가 제거된 결과 출력')
print(tokens_ko)

# A Text is typically initialized from a given document or corpus. E.g.:
ko = nltk.Text(tokens=tokens_ko, name='대한민국 헌법')

print('\ntype(ko)')
print(type(ko))  # <class 'nltk.text.Text'>

# <class 'nltk.probability.FreqDist'>
# (빈도수를 저장하고 있는 사전)
print('\ntype(ko.vocab())')
print(type(ko.vocab()))

print('\ntype(ko.vocab().most_common(50))')
print(type(ko.vocab().most_common(50)))  # <class 'list'>

print('ko.vocab().most_common(10)')
print(ko.vocab().most_common(10))

data = ko.vocab().most_common(500)
tmp_dict = dict(data)  # list를 사전으로 변경
print(tmp_dict)

alice_color_file = 'alice_color.png'
alice_color_mask = np.array(Image.open(alice_color_file))

# 윈도우 폴더 : c:\windows\fonts에 파일이 있습니다.
fontpath = 'malgun.ttf'
wordcloud = WordCloud(font_path=fontpath, mask=alice_color_mask,
                      relative_scaling=0.2, background_color='white')
wordcloud = wordcloud.generate_from_frequencies(tmp_dict)

image_color = ImageColorGenerator(alice_color_mask)

newwc = wordcloud.recolor(color_func=image_color, random_state=42)

plt.imshow(newwc, interpolation='bilinear')
plt.axis('off')

filename = 'national.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' 파일이 저장되었습니다.')

# plt.show()
print('finished')
