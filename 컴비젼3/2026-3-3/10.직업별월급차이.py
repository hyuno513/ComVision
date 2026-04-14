import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# openpyxl 설치 필요
welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_05.csv')

# 06. 직업별 월급 차이 - 어떤 직업의 월급이 가장 많이 받을까?
# 직업별 월급 분석을 위해 직업 변수를 검토하고 전처리
# 월급 변수는 미리 완료했으니 생략

# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 직업코드 / 월급
# 2단계 : 변수 간 관계 분석
# 직업별 월급 평균표 만들기 / 그래프 만들기

# 1. 직업 변수 검토 및 전처리하기
# 1) 변수 검토하기
print(welfare['code_job'].dtypes) # float64
print(welfare['code_job'].value_counts())

# code_job의 변수의 값은 직업 코드를 의미
# 직업 코드로는 어떤 작업을 의미하는지 알 수 없음으로 직업 이름을 나타낸 변수를 만들어야 함

# 2) 전처리하기
# 코드북의 직업분류코드 목록을 이용해 직업 이름을 나타낸 변수를 만듦
# 코드북의 '직종코드' 시트에 있는 직업분류코드 목록을 불러옴
list_job = pd.read_excel('./input/Koweps_Codebook_2019.xlsx', sheet_name='직종코드')
print(list_job.head())

print(list_job.shape) # 156, 2

# 출력 결과를 보면 직업분류코드 목록은 코드와 직업명 두 변수로 구성이 되고 직업이 156개로 분류

# df.merge를 이용해 list_job을 welfare에 결합
# welfare와 list_job에 공통으로 들어 있는 code_job 변수를 기준으로 결합

# welfare에 list_job 결합하기
welfare = welfare.merge(list_job, how='left', on='code_job')

# welfare의 code_job, job 변수 일부를 출력해 잘 결합되었는지 확인
# 출력할 때 작업이 결측치인 행은 제외
print(welfare.dropna(subset=['code_job'])[['code_job', 'job']].head())

welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_06.csv', mode='w')