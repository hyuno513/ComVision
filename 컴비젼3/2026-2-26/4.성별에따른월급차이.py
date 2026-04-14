import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv')

# 3. 성별에 따른 월급차이 분석
# 1) 성별 월급 평균표 만들기
# incomes 결측치 제거 : dropna(subsets['income'])
# sex별 분리 : groupby('sex', as_index=False)
# incomes 평균 구하기 : agg(mean_income('income', 'mean')
sex_income = welfare.dropna(subset=['income']).groupby('sex', as_index=False).agg(mean_incomes=('income', 'mean'))
print(sex_income)
# 평균 남자 월급은 349만원, 여자 월급은 186만원으로, 남성이 여성보다 많음

# 2) 그래프 만들기
# 분석 결과를 쉽게 이해할 수 있도록 성별 월급 평균표를 이용해 막대 그래프로 만듬