# 1. 2단 행렬 만들기
# np.arange와 reshape를 활용하여 다음과 같은 형태의 2차원 배열을 생성하세요
# 조건: 2부터 시작하여 2씩 증가하는 숫자들로 구성되어야 한다.
# 형태: 3행 4열
# 출력 예시
# [[ 2 4 6 8]
#  [10 12 14 16]
# [18 20 22 24]]

import numpy as np

a1 = np.arange(2,26,2)
print(a1)

a2 = np.arange(2,26,2).reshape(4,3)
print(a2)


# 문제2 "가짜 데이터 정제하기 (astype)
# 서버에서 받아온 데이터가 문자열 배열로 되어 있습니다. 이를 계산 가능한 정수(int)형 배열로 변환하세요.
# 조건: 아래의 dirty_data를 먼저 선언하고 시작하세요.
# 출력 예시 : [10 20 30 40 50] (타입은 int32 또는 int64)

dirty_data = np.array(['10.5', '10.1', '30.9', '41.2', '50.0'])
data2 = dirty_data.astype(float)
data3 = data2.astype(int)
print(data3)


