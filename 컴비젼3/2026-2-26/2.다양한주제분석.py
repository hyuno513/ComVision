# 다양한 분석 주제를 다루는데 분석마다 2단계로 진행

# 1단계 : 변수 검토 및 전처리
# 분석에 활용할 변수를 전처리
# 변수의 특징을 파악하고 이상치와 결측치를 정제한 다음, 변수의 값을 다루기 편하게 바꿈
# 전처리는 분석에 활용할 변수 각각 진행

# 2단계 : 변수 간 관계 분석
# 전처리를 완료하면 본격적으로 변수 간 파악하는 분석을 함
# 데이터를 요약한 표와 데이터의 특징을 쉽게 이해할 수 있는 그래프를 만든 다음 분석 결과를 해석

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 02. 성별에 따른 월급 차이 - 성별에 따라 월급이 다를까?
# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 성별 / 월급
# 2단계 : 변수 간 관계 분석
# 성별 월급 평균표 만들기 / 그래프 만들기

# 1) 성별 변수 검토 및 전처리하기
# 2) 변수 검토하기

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_01.csv')

# sex 성별 변수의 타입을 파악
print(welfare['sex'].dtypes)

# value_counts()를 이용해 각 범주마다 몇 명이 있는지 알아봄
print(welfare['sex'].value_counts())

# 2) 전처리하기
# 코드북을 보면 성별 변수의 값이 1이면 남자, 2면 여자를 의미, 모른다고 답하거나 응답하지 않으면 9로 입력
# 이 정보를 바탕으로 데이터에 이상치가 있는지 검토, 분석할 때 제거하기 편하도록 NAN을 부여해 결측치 처리
# 즉 값이 9인 경우 성별을 알 수 없어 분석에서 제외해야 하므로 결측처리

# 이상치 확인

# 1,2 만 있고 9나 다른 값이 없으니 이상치를 결측 처리하는 절차를 건너뛰어도 됨
# 만일 이상치가 있다면 이상치를 결측 처리한 후에 다음 결측치 확인

# 이상치 결측 처리
# sex 열에서 9인 값을 NAN으로 변경
print(welfare['sex'].isna().sum()) # 0

# 성별이 1,2로 되어 있어 값의 의미를 이해하기 어려우므로 문자 male과 female로 변경
# 변경 후 잘 반영이 되었는지 value_counts()와 countplot()를 이행?해 바꾼 값이 잘 반영이 되었는지 출력 결과를 확인
# 성별에 항목 이름 부여

welfare['sex'] = np.where(welfare['sex'] == 1, 'male', 'female')

# 빈도 구하기
print(welfare['sex'].value_counts())

# 빈도 막대 그래프 만들기
sns.countplot(data=welfare, x='sex')
plt.show()

# 작업한 데이터프레임을 csv로 저장
welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv', mode='w')

