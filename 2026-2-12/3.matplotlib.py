# 파이썬에서 데이터를 효과적으로 시각화하기 위해 만든 라이브러리
# matplotlib는 MATLAB (과학 및 공학 연산을 위한 소프트웨어)의 시각화 기능을 모델링해서 만들어짐
# 공식 홈페이지 : https://matplotlib.org/

import matplotlib.pyplot as plt

# 1. 선 그래프
# 1) 기본적인 선 그래프 그리기
# 선 그래프는 그래프 중 가장 기본이 되는 그래프
# 순서가 없는 수치 데이터를 시각화하거나 시간에 따라 변하는 수치 데이터를 시각화하는데 많이 사용

# 기본 형식 : plt.plot([x,] y [.fmt])
# x와 y는 각각 x축과 y축 좌표의 값을 의미
# x와 y는 시퀀스 길이가 같아야 함
# x와 y 데이터 중에서 x는 생략 가능. x가 없다면 x는 0부터 y의 개수만큼 1씩 증가하는 값으로 자동 할당
# fmt는 format string으로 다양한 형식으로 그래프를 그릴 수 있는 옵션

data1 = [10,14,19,20,25]
plt.plot(data1)
plt.show()


import numpy as np

x = np.arange(-4.5,5,0.5) # 배열 x 생성. 범위 :[-4.5,5], 0.5씩 증가
y = 2 * x ** 2 # 수식을 이용해 배열 x에 대응하는 배열 y를 생성
print([x,y])
plt.plot(x, y)
plt.show()