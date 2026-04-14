# 워드 클라우드를 이용한 데이터 시각화
# 텍스트 시각화에 이용
# 텍스트 데이터에서 출현 빈도가 높은 단어는 크게 표시하고 출현 빈도가 낮은 단어는 작게 표시하는 방법으로 데이터 시각화

from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_name = './input_data/littleprince_djvu.txt'
with open(file_name) as f:
    text = f.read()

# 워드 클라우드의 이미지를 생성
wordcloud_image = WordCloud().generate(text)

# 생성한 워드 클라우드 이미지를 화면에 표시
plt.imshow(wordcloud_image, interpolation='bilinear') # interpolation='bilinear' -> 이미지를 부드럽게 처리
plt.axis('off')
plt.show()

# 옵션 지정도 가능
# 배경 변경 가능, 최대 글자크기 지정 가능, 가로 세로 픽셀 지정 가능
wordcloud_image = WordCloud(background_color='white', max_font_size=300, width=800, height=400).generate(text)
plt.imshow(wordcloud_image, interpolation='bilinear')
plt.axis('off')
plt.show()

image_file_name = './output_data/little_prince.png'
wordcloud_image.to_file(image_file_name)
plt.show()

import numpy as np
from PIL import Image

mask = np.array(Image.open('./input_data/image.jpg'))
wordcloud_image = WordCloud(background_color='white', max_font_size=300, mask=mask, contour_color='gold', colormap='copper').generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud_image, interpolation='bilinear')
plt.axis('off')
plt.show()

# 한글 단어와 빈도 데이터의 워드 클라우드 이미지를 생성하는 예
# 한글 단어와 빈도가 저장된 데이터 파일을 DataFrame 형식으로 읽어옴
import pandas as pd
word_count_file = './input_data/word_count.csv'
word_count = pd.read_csv(word_count_file)
print(word_count.head(5))

print(word_count['빈도'][0:5])

korean_font_path = 'C:/Windows/Fonts/malgun.ttf' # 한글 폰트 선택(맑은 고딕) 파일명


## 오류뜸
# 워드 클라우드 이미지 생성
wc = WordCloud(font_path=korean_font_path, background_color='white')
frequencies = word_count('단어')['빈도'].to_dict() # pandas의 Series 형식이 됨
wordcloud_image = wc.generate_from_frequencies(frequencies)

# 생성한 워드 클라우드 이미지를 화면에 표시
plt.imshow(wordcloud_image, interpolation='bilinear')
plt.axis('off')
plt.show()