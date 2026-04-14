import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_04.csv')

# 01. 연령대 및 성별 월급 차이 - 성별 월급 차이는 연령대별로 다를까?

# 성별에 따라 월급 차이가 있는지 분석
# 그런데 성별 월급 차이는 연령대에 따라 다른 양상을 보일 수 있음
# 성별 월급 차이가 연령대에 따라 어떻게 다른지 분석
# 연령대, 성별, 월급 변수 모두 앞에서 전처리 작업을 완료 했으므로 전처리 작업 생략

# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 연령대 / 성별 / 월급
# 2단계 : 변수 간 관계 분석
# 연령대 및 성별 월급 평균표 만들기 / 그래프 만들기

# sex_income =
sex_income = welfare.dropna(subset=['income']).groupby(['age', 'sex'], as_index=False).agg(mean_incomes=('income', 'mean'))
print(sex_income)
#       age     sex     mean_incomes
# 0     middle  female
# 1     middle  male
# 2
# 3
# 4
# 5

# 막대그래프 만들기
sns.barplot(data=sex_income, x='age', y='mean_incomes', hue='sex', order=['young', 'middle', 'old'])
plt.show()

# 2. 나이 및 성별 월급 차이 분석하기

sex_age = welfare.dropna(subset=['income']).groupby(['age', 'sex'], as_index=False).agg(mean_income=('income', 'mean'))
print(sex_age.head())
#   age     sex     mean_income
# 0     middle    male
# 1     middle    female
# 2     old    male

sns.lineplot(data=sex_age, x='age', y='mean_income', hue='sex')
plt.show()

welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_05.csv')
