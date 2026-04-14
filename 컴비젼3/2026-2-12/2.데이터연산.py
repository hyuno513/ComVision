# 2. 데이터 연산
# pandas와 Series()와 Dataframe()으로 생성된 데이터 끼리는 사칙연산이 가능
# Series()로 생성한 데이터의 예

import pandas as pd
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
print(s1 + s2)
print(s2-s1)

# 중요 * : 파이썬의 리스트와 numpy의 배열과 달리 pandas의 데이터기리는 서로 크기가 달라도 연산이 가능하다
# 이 경우 연산을 할 수 있는 항목만 연산을 수행
s3 = pd.Series([1,2,3,4])
s4 = pd.Series([10,20,30,40,50])
print(s3 + s4)
