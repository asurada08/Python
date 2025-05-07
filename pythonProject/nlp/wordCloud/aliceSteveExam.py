import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud

image_file = 'alice.png'

img_file = Image.open(image_file)
print(type(img_file))
print('-' * 40)

alice_mask = np.array(img_file)

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask)

textfile = 'heart-of-darkness.txt'
text = open(textfile, 'rt', encoding='utf-8')
text = text.read()

wc = wc.generate(text)  
print(wc.words_)  

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

filename = 'heart-of-darkness.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' 파일이 저장되었습니다.')
print('작업 종료')