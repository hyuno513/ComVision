# 1. 직업별 월급 차이 분석
# 1) 직업별 월급 평균표 만들기
# 직업이 없거나 월급을 받지 않는 사람은 분석 대상이 아니므로 제외

# 직업별 월급 평균표 만들기
# 결측치 제거
# income 평균 구하기

# 2) 그래프 만들기
# a) 월급이 많은 직업
# 요약표를 월급 기준으로 정렬하고 내림차순 상위 10개를 추출

# 상위 10위 추출

# 막대 그래프 만들기

# b) 월급이 적은 직업
# 요약표를 월급 기준으로 오름차순 정렬하고 하위 10개를 추출

# 하위 10위 추출

# 막대그래프 만들기
# 앞에서 만든 월급 상위 10위 그래프와 비교할 수 있도록 그래프의 x축을 0 ~ 800으로 제한

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc # 폰트 세팅을 위한 모듈 추가
font_path = "C:/Windows/Fonts/malgun.ttf" # 사용할 폰트명 경로 삽입
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)
welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_06.csv')


job_income = welfare.dropna(subset=['job','income']).groupby('job', as_index=False).agg(mean_income=('income', 'mean'))
job_income = job_income.sort_values(by='mean_income', ascending=False)
job_income_1 = job_income.head(10)
print(job_income_1)
plt.figure(figsize=(16,9))
sns.barplot(data=job_income_1, x='mean_income', y='job').set(xlim=(0,800))
plt.show()

job_income_2 = job_income.sort_values(by='mean_income', ascending=True)
job_income_2 = job_income_2.head(10)
print(job_income_2)

sns.barplot(data=job_income_2, x='mean_income', y='job').set(xlim=(0,800))
plt.show()
