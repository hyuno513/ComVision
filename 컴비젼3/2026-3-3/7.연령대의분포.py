import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 01. 연령대에 따른 월급 차이 - 어떤 연령대의 월급이 가장 많을까?
# 나이별 월급 평균을 분석했고, 나이를 연령대로 분류한 다음 평균을 비교

# 분석 절차
# 1단계: 변수 검토 및 전처리
# 연령대 / 월급
# 2단계 : 변수 간 관계 분석
# 연령대별 월급 평균표 만들기 / 그래프 만들기

# 1. 연령대 변수 검토 및 전처리하기
# 1) 파생변수 만들기 - 연령대
# 나이 변수를 이용해 연령대 변수를 만듦
# 아래 기준에 따라 연령대 변수를 만든 다음 각 범주에 몇 명이 있는지 살펴봄

# 범주 : 기준
# 초년층 : 30세 미만
# 중년층 : 30~59세
# 노년층 : 60세 이상

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_03.csv')

# 0. 나이 변수 살펴보기
print(welfare['age'].describe())
print(welfare['age'])
# 1 72.0
# 2 78.0
# 3 58.0
# 4 57.0
# Name : age, dtype: float64


# 1. # 연령대 변수 만들기 hint : assign 메소드 확인
welfare = welfare.assign(age=np.where(welfare['age'] < 30, 'young', np.where(welfare['age'] <= 59, 'middle', 'old')))


# 2. # 빈도 구하기
# old 5955
# middle 4963
# young 3500
# Name : ageg, dtype: int64
print(welfare['age'].value_counts())
# 3. # 빈도 막대 그래프 만들기
sns.countplot(data=welfare, x='age')
plt.show()
welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_04.csv')

