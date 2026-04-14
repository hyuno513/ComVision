# 문제 : 나이와 월급의 평균표를 나타내시오 (나이에 따른 월급차이분석)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_03.csv')

# 나이별 월급 평균표
age_income = welfare.dropna(subset=['income']).groupby('age').agg(mean_income=('income', 'mean'))
print(age_income)

# 선그래프 만들기
sns.lineplot(data=welfare, x='age', y='mean_income') ## 오류??
plt.show()
