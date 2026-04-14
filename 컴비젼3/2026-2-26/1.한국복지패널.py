# 한국복지패털 데이터 분석

# 한국복지패널 데이터는 한국보건사회연구원에서 우리나라 가구의 경제활동을 연구해
# 복지 정책에 반영할 목적으로 발간하는 조사 자료
# 전국에서 7000여 가구를 선정해 2006년 부터 매년 추적한 조사 자료로
# 경제활동, 생활실태, 복지욕구 등 천여 개 변수로 구성되어 있음
# 다양한 분야의 연구자의 정책 전문가들이 복지패널 데이터를 활용해 논문과 연구보고서를 발표하고 있음
# 한국복지패널 데이터는 엄밀한 절차에 따라 수집되었고 다양한 변수를 담고 있으므로 데이터 분석을 연습하는데 훌륭한 재료
# 데이터에는 다양한 삶의 모습이 담겨져 있어서 대한민국 사람들이 이렇게 살고 있는지 살펴볼 수 있음

# 1. 한국복지패널 데이터 분석 준비하기

# https://www.koweps.re.kr:442/data/data/list.do

# 1) 데이터 준비하기 Koweps_hpwc14_2019_beta2.sav

# 2) 패키지 설치 및 로드하기
# 데이터 파일은 통계 분석 소프트웨어인 SPSS 전용파일
# pyreadstat 패키지를 설치하면 pandas 패키지의 함수를 이용해 SPSS, SAS, STATA 등 다양한 통계 분석
# 소프트웨어의 데이터 파일을 불러올 수 있음
# pip install pyreadstat

import pandas as pd
import numpy as np
import seaborn as sns # 데이터 시각화 라이브러리

# 3) 데이터 불러오기
# 데이터 원본은 복구할 상황을 대비해 그대로 두고 복사본을 만들어 분석에 활용하는 것이 좋다

raw_welfare = pd.read_spss('./input/Koweps_hpwc14_2019_beta2.sav')
welfare = raw_welfare.copy()

# 4) 데이터 검토하기
# 데이터 구조와 특징을 파악
print(welfare)
print(welfare.shape) # 행, 열 개수 분석

print(welfare.info()) # 변수 속성 출력

print(welfare.describe()) # 요약 통계량

# 복지패널 데이터와 같은 대규모 데이터는 변수의 수가 많고 변수명이 코드로 되어 있어
# 전체 구조를 한 눈에 파악하기 어려움
# 규모가 큰 데이터는 데이터 전체를 한 번에 파악하기보다 변수명을 쉬운 단어로 바꾼 다음
# 분석에 사용할 변수를 하나씩 살펴봐야 함

print(welfare.head(2))

# 5) 변수명 바꾸기
# 규모가 큰 조사 자료는 데이터의 특징을 설명해 놓은 codebook을 통해 제공
# 코드북에는 코드로 된 변수명과 값의 의미가 설명되어 있음
# 코드북을 보면 데이터의 특징이어떠한지 감을 잡을 수 있고, 분석에 어떤 변수를 활용할지, 분석 방향의 아이디어를 얻을 수 있음
# 코드북의 파일명은 Koweps_Codebook_2019.xlsx

# 코드북을 참고해 분석에 사용할 변수 7개의 이름을 알기 쉬운 단어로 바꿈
welfare = welfare.rename(columns=
{
    'h14_g3' : 'sex', # 성별
    'h14_g4' : 'birth', # 태어난 연도
    'h14_g10' : 'marriage_type', # 혼인 상태
    'h14_g11': 'religion', # 종교
    'p1402_8aq1': 'income', # 월급
    'h14_eco9': 'code_job', # 직업 코드
    'h14_reg7': 'code_region' # 지역 코드
}) # 안의 변수명을 바꿔주는 메소드

print(welfare.columns)

welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_01.csv', mode='w')

