# 문제1. BMI 지수 계산기
import numpy as np

weights = np.array([65,78,92,55,80])
heights = np.array([170,180,185,168,175])

# 요구사항 : height 배열을 m단위로 변환한 뒤 BMI를 구하시오.

heights2 = heights/100
print(heights2)

heightsquare = heights2**2

bmi = weights/heightsquare
print(bmi)


# 문제 2번
# 한 학급의 시험 점수 데이터가 있습니다. 통계를 내시오
scores = np.array([82,95,77,45,99,88,60,100,52,70])
# 요구사항
# 1. 학급 전체의 평균점수를 출력
# 2. 점수가 80점 이상인 데이터만 True로 표시되는 불린 배열을 출력
# 3. 학급에서 최고점을 받은 점수를 촐력

print(scores.mean())
print(scores >= 80)
print(scores.max())


# 문제3
# 어느 가게의 1월부터 6월까지의 월별 데이터 매출입니다.
sales = np.array([120,150,90,200,250,180])
# 요구사항
# 1. 상반기 총 매출합계를 구하시오
# 2. 매달 매출이 합쳐지는 누적 매출 배열을 생성하시오.

print(sales.sum())
print(sales.cumsum())
