import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv')

# 2. 월급 변수 검토 및 전처리하기
# 1) 변수 검토하기
# 코드북을 보면 월급은 '일한 달의 평균 임금'을 의미하며 1만원 단위로 기록
# 변수 이름은 income
# 성별은 범주 변수이므로 df.value_account()를 이용해 범주별 빈도를 확인하면 특징을 파악할 수 있음
# 하지만 월급은 연속 변수이므로 df.value_account()을 이용하면 너무 많은 항목이 출력되어 알아보기 어려움
# 연속변수는 df.describe()로 요약 통계량을 확인해야 특징을 파악할 수 있음

print(welfare['income'].dtypes)
print(welfare['income'].describe())

# 출력 결과를 보면 float64 타입이고, 0~1892만원의 값을 지님
# 150 ~ 345만원에 가장 많이 분포하고 평균은 268만원, 중앙값은 평균보다 작은 220만원으로
# 전반적으로 낮은 쪽에 치우침

# 히스토그램을 만들어서 분포를 확인
sns.histplot(data=welfare, x='income')
plt.show()

# 2) 전처리하기
# 코드북을 보면 월급은 만원 단위로 되어 있고, '모름/무응답=9999'

print(welfare['income'].isna().sum()) # 결측치 확인

# 출력 결과를 보면 최소값은 0 ~ 1892고 결측치 9884건이 있음
# 즉 9999가 입력된 데이터는 X
# 이상치를 결측 처리하는 절차를 건너뛰어도 됨

# 만약 9999인 항목이 있다면 아래와 같이 이상치를 결측 처리하는 절차를 거쳐야 함
# 이상치 결측 처리
welfare['income'] = np.where(welfare['income'] == 9999, np.nan, welfare['income'])

# 결측치 확인
print(welfare['income'].isna().sum())

welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv', mode='w')