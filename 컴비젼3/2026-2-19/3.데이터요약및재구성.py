# 데이터의 요약 및 재구성

# 1) 데이터의 구조 살펴보기
# DataFrame 데이터를 요약하고 데이터의 개수를 세는 방법

# DataFrame 형식 데이터의 전체 구조를 알아보려면 info()를 이용
# DataFrame_data.info()

# DataFrame 데이터의 index와 columns의 타입을 보여주고, 결측치가 아닌 값의 개수와 메모리 사용량 정보를 요약해서 보여줌

import pandas as pd

data_file = './input_data/total_sales_data.csv'

df_sales = pd.read_csv(data_file)
print(df_sales)

print(df_sales.info())

# 출력 결과를 보면 index의 범위는 0 ~ 8 까지 9개
# 열(Column)은 총 5개
# 열 데이터에서 매장명, 제품종류, 모델명의 데이터 타입은 객체(object)이고
# 판매 및 재고의 데이터 타입은 정수(int64)
# 메모리 사용량은 컴퓨터마다 다름

# pandas의 Series 형식의 데이터에서 중복되지 않는 값이 몇 개인지 알아보려면 value_counts()를 이용
# Series_data.value_counts()

# DataFrame 데이터에서 특정 열을 선택한 후에 value_counts()를 이용하면 해당 열의 데이터 값의 개수를 알 수 있음

# df_sales에 할당된 값에서 매장명이 들어있는 데이터 값의 각 개수를 알고 싶을 때 사용
print(df_sales['매장명'].value_counts())

# df_sales 변수의 매장명 열에는 데이터 값이 'A', 'B', 'C'가 있으며 각각 3개씩 데이터가 있음
print(df_sales['제품종류'].value_counts())

# 제품종류 열에는 데이터 값이 '스마트폰'과 'TV'가 있으며 나오는 횟수는 각각 5, 4회

# 2) 피벗 테이블로 데이터 재구성하기
# DataFrame 데이터를 원하는 그룹별로 재구성한 후 원하는 값을 계산하는 방법
# 데이터를 재구성하면 데이터를 좀 더 직관적으로 표시할 수 있어서 이해하기 쉬움

# pivot_table()은 DataFrame 데이터를 보기 쉽게 재구성하거나 데이터에서 특정 열에 있는 값이 나온 횟수를 구하거나
# 평균을 구하는 등 계산이 필요한 경우에 주로 사용
# 엑셀의 피벗 테이블과 유사한 기능

# DataFrame_data.pivot_table(values=None, index=None, columns=None, aggfunc='mean')

# values는 재구성할 데이터의 열 이름이 들어감
# index와 columns에는 각각 피벗 테이블의 index와 columns에 들어갈 데이터의 열이름이 들어감

print(df_sales.pivot_table(index=['매장명', '제품종류', '모델명'], values=['판매', '재고'], aggfunc='sum'))

# 재고와 판매수량이 매장명, 제품종류, 모델명에 따라 보기 좋게 정리

# 매장별로 제품 종류에 따른 재고 와 판매 수량을 알고 싶을 때

print('매장별로 제품 종류에 따른 재고와 판매한 모델의 개수')
print(df_sales.pivot_table(index=['매장명'], columns=['제품종류'], values=['판매', '재고'], aggfunc='count'))