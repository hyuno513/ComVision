import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv')

# 3. 나이와 월급의 관계 = 몇 살 대 월급을 많이
# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 나이 / 월급
# 2단계 : 변수 간 관계 분석
# 나이에 따른 월급 평균표 만들기 / 그래프 만들기

# 1. 나이 변수 검토 및 전처리하기
# 1) 변수 검토하기
# 나이 변수는 없고 태어난 연도 변수만 있음
# 따라서 태어난 연도 변수를 기반으로 나이 변수를 만들어야함

print(welfare['birth'].dtypes)

print(welfare['birth'].describe())

sns.histplot(data=welfare, x='birth')
plt.show()

# 2) 전처리
# 코드북을 보면 태어난 연도는 '모름/무응답=9999' 이다.
# 이를 바탕으로 전처리

# 결측치 확인
print(welfare['birth'].isna().sum()) # 0

# 이상치와 결측치가 없으므로 파생변수를 만드는 다음단계로 넘어감
# 만일 이상치가 발견되면 아래와 같이 전처리 한 다음 분석을 진행

# 이상치 결측 처리
welfare['birth'] = np.where(welfare['birth'] == 9999, np.nan, welfare['birth'])

# 결측치 확인
print(welfare['birth'].isna().sum())

# 나이 변수 만들기
# df.assign(kwargs) : DataFrame에 열을 할당하는 메서드.
# # kwargs : 새 열이름 = 내용 형식으로 입력되는 키워드
welfare = welfare.assign(age=2019 - welfare['birth'])
# 통계량 구하기
print(welfare['age'].describe())

# 히스토그램 만들기
sns.histplot(data=welfare, x='age')
plt.show()

welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_03.csv')