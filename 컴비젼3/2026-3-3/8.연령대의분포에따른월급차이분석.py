import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_04.csv')

# 1. 연령대별 월급 평균표 만들기
# 1.1 income 결측치 제거
# 1.2 age별 분리
# 1.3 income 평균 구하기

print(welfare['income'].isna().sum())

age_income = welfare.dropna(subset=['income']).groupby('age', as_index=False).agg(mean_income=('income', 'mean'))
print(age_income)

# 출력 결과
#       age mean_income
# 0     middle  329.
# 1     old     140.
# 2     young   195.

# 2. 그래프 만들기
# 평균표를 이용해 그래프 작성, x축을 나이, y축을 월급으로 지정해 나이에 따른 월급의 변화를 나타낸 선그래프 만듦

# 선그래프 만들기
sns.lineplot(data=age_income, x='age', y='mean_income')
plt.show()