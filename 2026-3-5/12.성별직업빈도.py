# 성별 직업 빈도 = 성별로 비교를 하였을 때 어던 직업이 가장 많을까?
# 성별, 직업 변수 전처리 작업은 앞에서 했으니 패스

# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 성별 / 직업
# 2단계 : 변수 간 관계 분석
# 성별 직업 빈도표 만들기 / 그래프 만들기

# 1. 성별 직업 빈도 분석
# 1) 성별 직업 빈도표 만들기

# 남성 직업 빈도 상위 10개 추출

# 여성 작업 빈도 상위 10개 추출

# 그래프 만들기(막대 그래프, x = 인구수, y = job)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc # 폰트 세팅을 위한 모듈 추가
font_path = "C:/Windows/Fonts/malgun.ttf" # 사용할 폰트명 경로 삽입
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_06.csv')


# 1. 데이터 로드 및 전처리 (결측치 제거)
job_male = welfare.dropna(subset=['job']) \
    .query("sex == 'male'").groupby('job', as_index=False) \
    .agg(n=('job', 'count')) \
    .sort_values('n', ascending=False) \
    .head(10)
job_female = welfare.dropna(subset=['job']) \
    .query("sex == 'female'").groupby('job', as_index=False) \
    .agg(n=('job', 'count')) \
    .sort_values('n', ascending=False) \
    .head(10)
print(job_male)
print(job_female)

# 안뜸??
# 2. 남성 직업 빈도 상위 10개 추출
# top10_male = job_male['job'].value_counts().head(10).reset_index()
# top10_male.columns = ['job', 'count']
#
# # 3. 여성 직업 빈도 상위 10개 추출
# top10_female = job_female['job'].value_counts().head(10).reset_index()
# top10_female.columns = ['job', 'count']
# # 결과 확인
# print('print')
# print(top10_male)
# print(top10_female)

# sns.barplot(data=top10_male, x='job', y='count')
# plt.show()

sns.barplot(data=job_male, x='n', y='job')
plt.show()

sns.barplot(data=job_female, x='n', y='job')
plt.show()