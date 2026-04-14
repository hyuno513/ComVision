# 1. 파이그래프
# 파이 그래프는 원 안에 데이터의 각항목이 차지하는 비율만큼 부채꼴의 크기를 갖는 영역으로 이루어진 그래프
# 각 부채꼴 부분이 파이 조각처럼 생겨서 파이 그래프라고 함
# 파이 그래프에서 부채꼴 부분의 크기는 각 항목의 크기에 비례
# 전체 데이터에서 각 항목이 차지한 비율을 비교할 대 많이 이용

# plt.pie(x [, labes=label_seq, autopct='비율 표시 형식(ex: 0.1%f)', shadow=False(기본) 혹은 True
# , explode=explode_seq, countercolock=True(기본) 혹은 False, startangle=각도 (기본은 0)])

# x는 배열 확인 시퀀스 형태의 데이터
# pie()는 x를 입력하면 x의 각 요소가 전체에서 차지하는 비율을 계산하고 그 비율에 맞게 부채골 크기를 결정해서 파이 그래프를 그림

# labels : x데이터 항목의 수와 같은 문자열 시퀀스(리스트, 튜플)을 지정해 파이 그래프의 각 부채꼴 부분에 문자열을 표시

# autopct : 각 부채꼴 부분의 항목의 비율이 표시되는 숫자의 형식을 지정
# 예를 들어 '%0.1f'가 입력되면 소수점 첫재 자리까지 표시되며, '%0.0f'가 입력되면 정수만 표시

# shadow : 그림자 효과를 지정. 기본 값은 False

# explode : 부채꼴 부분이 원에서 돌출되는 효과를 주어 특정 부채꼴 부분을 강조할 때 이용
# x 데이터 항목의 수와 같은 문자열 시퀀스(리스트, 튜플)을 지정. 기본 값을 강조 효과가 없음

# counterClock : x 데이터에서 부채꼴 부분이 그려지는 순서가 반시계방향(True)인지 시계방향(False)인지를 지정
# 기본값은 True로 반시계 방향

# startangle : 제일 처음 부채꼴 부분이 그려지는 각도로 x축을 중심으로 반시계 방향으로 증가. 기본값은 0


import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]

plt.pie(result)
plt.show()

# 비율을 맞춰 출력
plt.figure(figsize=(5, 5))
plt.pie(result)
plt.show()

# 각 부채골 부분에 속하는 데이터의 라벨과 비율을 추가
plt.figure(figsize=(5, 5))
plt.pie(result, labels=fruit,autopct='%.1f%%')
plt.show()

# 각 부채꼴 부분은 x축 기준 각도 0도를 시작으로 반시계방향으로 그려짐
# x축 기준 각도 90도에서 시작해서 시계방향으로 그리는 예
plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='&.1f%%', startangle=90, counterclock=False)
plt.show()

# 그림자를 추가하고 특정 요소(사과)를 표시한 부채꼴 부분만 강조한 예
explode_value = (0.1,0,0,0,0)
# 0.1 : 반지름의 10% 만큼 벗어나도록 설정

plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='&.1f%%', startangle=90, counterclock=False, explode=explode_value, shadow=True)
plt.show()


# 문제----
# 문제 1. 기본 파이 그래프 완성하기
# 당신은 좋아하는 운동 종목에 대한 설문조사 결과를 시각화해야 합니다. 아래의 조건을 만족하는 코드를 작성하시오
# 데이터 : * 항목(sports): ['축구', '농구', '배구']
# 수치(data) : [95, 3, 2]
# 조건:
# 각 부채골에 운동 종목 이름을 라벨로 표시하세요
# 비율을 소수점 첫째 자리까지 표시하세요 (예: 40.0%)

# 문제2. 시계 방향 및 시작 각도 설정하기
# 위 1번 문제의 데이터를 그대로 사용하되, 시각적인 배치를 아래와 같이 수정하세요
# 조건:
# 그래프의 시작 각도를 12시 방향(90도)으로 설정하세요
# 데이터가 시계 방향으로 배치되도록 설정하세요
# 그래프에 그림자(shadow) 효과를 추가하세요

# 문제3. 특정 항목 강조 및 레이아웃 조정
# 가장 응답률이 높은 '축구' 항목을 강조하고 싶습니다. 다음 조건을 반영하여 코드를 완성하세요
# 조건:
# explode 기능을 사용하여 '축구' 조각을 원에서 0.1만큼 돌출시키세요
# 전체 그래프의 크기를 가로 7,  세로 7 인치로 설정하세요


sports = ['축구', '농구', '배구']
data = [97, 2, 1]
plt.figure(figsize=(7, 7))
plt.pie(data, labels=sports,autopct='%1.f%%')

plt.show()

explodevalue = (0.1, 0, 0)
plt.pie(data, labels=sports, autopct='%1.f%%', startangle=90, counterclock=False, explode=explodevalue, shadow=True)


# 제목 추가방법 : 제목 plt.title로 제목을 추가할 수 있다.
plt.title('선호하는 운동 종목')
plt.show()


# 1. 직접 색상 지정하기
# colors
fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]

# 색상 리스트 정의 (항목의 수와 맞추는 것이 좋음)
# 부족하면 색상이 순환하며 적용
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#ADD8E6']
plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='%.1f%%', colors=colors)

plt.title('과일별 선호도 (커스텀)')
plt.show()

import numpy as np

# 2. 컬러맵 지정하기
cmap = plt.get_cmap('Pastel1') # Paired, Accent 등 다양한 테마가 있음
colors = cmap(np.arange(len(fruit)))

plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='%.1f%%', colors=colors)
plt.title('과일별 선호도 (커스텀)')
plt.show()