# 2. 배열의 연산
import numpy as np

# 1) 기본 연산
# 배열의 형태 shape가 같다면 덧셈과 뺄셈, 곱셈과 나눗셈 연산을 할 수 있음

arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])

# 각 배열의 합은 같은 위치의 원소끼리 더함
print(arr1 + arr2)

# 두 배열의 차는 같은 위치의 원소끼리 뺌
print(arr1-arr2)
# 배열에 상수를 곱하면 각 원소에 상수를 곱함
print(arr1*2)
# 배열의 거듭제곱은 배열의 각 원소에 거듭제곱
print(arr1**2)
# 두 배열끼리의 곱셈은 각 원소끼리 곱합
print(arr1*arr2)
# 두 배열의 나눗셈은 각 원소끼리 나눔
print(arr1/arr2)

# 복합연산
print(arr1/(arr2**2)) # [10.          5.          3.33333333  2.5       ]

# 배열은 비교 연산도 가능. 원소별로 조건과 일치하는지 검사한 후 일치하면 True를, 그렇지 않으면 False를 반환
print(arr1 > 20) # [False False  True  True]

# 2) 통계를 위한 연산
# Numpy에는 배열의 합, 평균, 표준편차, 분산, 최솟값과 최댓값, 누적 합과 누적 곱 등 주로 통계에서 많이 이용하는 메서드가 있음
# 각각 sum(), mean(), std(), var(), min(), max(), cumsum(), cumprod()

arr3 = np.arange(5)
print(arr3)

# 합
print(arr3.sum()) # 10
# 평균
print(arr3.mean()) # 2.0
# 표준편차
print(arr3.std()) # 1.414213
# 분산
print(arr3.var()) # 2.0
# 최솟값
print(arr3.min()) # 0
# 최댓값
print(arr3.max()) # 4

arr4 = np.arange(1,5)
print(arr4) # [1 2 3 4]
# 누적 합
print(arr4.cumsum()) # [ 1  3  6 10]
# 누적 곱
print(arr4.cumprod()) # [ 1  2  6 24]



