# 2. 데이터 획득, 처리, 시각화 심화
# 2-1 데이터에서 결측치 확인 및 처리

# 결측치 확인:
# 결측치 : 데이터가 비어있거나 문제가 있는 데이터(더미데이터)

import pandas as pd

# csv 파일을 보면 2017, 2018 데이터만 결측치가 없고, 나머지 연도에는 모두 결측치가 있음을 확인
data_file = './input_data/missing_data_test.csv'
df = pd.read_csv(data_file, encoding='cp949', index_col='연도')
print(df)

# csv 파일의 결측치는 pandas의 DataFrame에서 데이터가 없음을 의미하는 NAN으로 표시

# isnull() : pandas메서드 : NAN이 있으면 True, 없으면 False를 반환
# 각 열에서 글측치 개수를 알고 싶다면 sum()을 이용
print(df.isnull().sum())
# True는 1, False는 0으로 간주해서 True의 개수를 반환

# 2. 결측치 처리
# 데이터에 결측치가 있으면 데이터 처리를 제대로 할 수 없으므로 결측치를 처리해야 함
# 1) 결측치가 있는 행이나 열을 없애거나 2) 결측치를 지정한 값으로 채움

# 1) 결측치가 있는 행이나 열을 없앰
# pandas의 DataFrame 형식의 데이터에서 drop()을 이용
# DataFrame_data.drop(index=index_name 혹은 columns=columns_name)

print(df.drop(index=[2019])) # index로 2019가 있는 행 전체를 제거

print(df.drop(columns=['제품3', '제품4'])) # index로 2019가 있는 행 전체를 제거

# pandas의 DataFrame 형식의 데이터에서 dropna()을 이용
# 결측치가 있는 행이나 열 전체를 없앰
# DataFrame_data.dropna(axis=0(기본) [, subset='행 또는 열이름'])

print(df.dropna())
print(df.dropna(subset=['제품4'])) # 제품4에 결측치가 있는 행만 없앰

print(df.dropna(axis=1)) # 결측치가 있는 모든 열을 제거
print(df.dropna(axis=1, subset=[2016, 2019])) # subset에 index 이름을 여러개 지정해서 결측치가 있는 열을 제거

# 2) 결측치를 지정한 값으로 채무
# DataFrame의 경우 fillna()를 이용해 결측치에 값을 채움
# DataFrame_data.fillna(value=None, method=None)
# value에는 결측치에 채워 놓고 싶은 값을 지정
# 가능한 형식은 하나의 수치나 문자열, 딕셔너리, pandas의 Series나 DataFrame
# 값을 지정하지 않고 method를 이용하면 주변의 값을 이용해 결측치를 채움
# method=bfill 이면 현재 위치의 결측치에 다음 위치의 데이터 값을 채우고
# method=ffill 이면 현재 위치의 결측치에 이전 위치의 데이터 값을 채움

print()
print(df.fillna(0)) # 결측치 전체를 0으로 채움

print(df.bfill())
# 마지막 값에 결측치가 있는 경우가 아니라면 다음 값을 이용해 현재 위치의 결측치를 채움

values = {'제품1': 100, "제품4": 400}
print(df.fillna(value=values)) # 지정한 열의 결측치만 측정한 값으로 채루 때
# 제품1 열의 결측치는 100으로 채워지고, 제품4 열의 결측치는 400으로 채워짐



