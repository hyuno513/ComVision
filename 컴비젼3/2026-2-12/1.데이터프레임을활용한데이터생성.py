# 1) DataFrame을 활용한 데이터 생성
# 표 Table과 2차원 데이터 처리를 위해 DataFrame을 제공
# 데이터 Data를 담는 틀 Frame 이라는 뜻

# DataFrame을 이용해 데이터를 생성하는 방법
# df = pd.DataFrame(data, [,index = index_data, columns = columns_data])
# data 인자에는 리스트와 형태가 유사한 데이터 타입은 모두 사용 가능
# 즉 리스트, 딕셔너리, numpy의 배열 데이터, Series나 DataFrame 타입의 데이터 입력 가능
# 세로축 라벨을 index라 하고, 가로축 라벨을 columns라고 함
# index의 columns를 제외한 부분을 values라고 하고 values가 관심있는 데이터

import pandas as pd

d1 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]])
print(d1)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
# values 부분에는 입력한 data가 순서대로 입력돼 있고
# 가장 좌측의 열과 가장 윗줄의 행에는 각각 숫자가 자동으로 생성되어 index, columns를 구성
# 명시적으로 index와 columns를 입력하지 않더라도 자동으로 index, columns가 생성

# numpy 의 배열 데이터를 입력해 생성한 DataFrame 데이터의 예
import numpy as np

data_list = np.array([[10,20,30], [40,50,60,], [70,80,90]])
d2 = pd.DataFrame(data_list)
print(d2)
#     0   1   2
# 0  10  20  30
# 1  40  50  60
# 2  70  80  90

# data뿐만 아니라 index와 columns도 지정한 예
data = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
index_date =pd.date_range('2026-02-15', periods=4)
columns_list = ['A', 'B', 'C']
d3 = pd.DataFrame(data, index=index_date, columns=columns_list)
print(d3)
#              A   B   C
# 2026-02-15   1   2   3
# 2026-02-16   4   5   6
# 2026-02-17   7   8   9
# 2026-02-18  10  11  12

# 딕셔너리 타입으로 2차원 데이터를 입력한 예
table_data = {'연도':[2022,2023,2024,2025,2026],
              '지사':['한국', '미국', '중국', '일본', '프랑스'],
              '고객수':[200,250,450,300,500]}
d4 = pd.DataFrame(table_data)
print(d4)
#      연도   지사  고객수
# 0  2022   한국  200
# 1  2023   미국  250
# 2  2024   중국  450
# 3  2025   일본  300
# 4  2026  프랑스  500

# 입력시 키의 순서를 지정할 수도 있음
d5 = pd.DataFrame(table_data, columns=['지사', '고객수', '연도'])
print(d5)
#     지사  고객수    연도
# 0   한국  200  2022
# 1   미국  250  2023
# 2   중국  450  2024
# 3   일본  300  2025
# 4  프랑스  500  2026

# DataFrame 데이터에서 index, columns, values를 각각 구한 예
print(d5.index) # RangeIndex(start=0, stop=5, step=1)
print(d5.columns) # Index(['지사', '고객수', '연도'], dtype='str')
print(d5.values)
# [['한국' 200 2022]
#  ['미국' 250 2023]
#  ['중국' 450 2024]
#  ['일본' 300 2025]
#  ['프랑스' 500 2026]]


# 문제1.

# 아래의 데이터와 조건을 사용하여 변수 df_fruit를 생성하고 출력하는 코드를 작성하시오
# Data : 2차원 리스트 [[1000,25],[1500,30],[500,50]]
# Index: 사과, 배, 수박
# columns: 가격, 재고

fruit = [[1000,25],[1500,30],[500,50]]
indexfruit = ['사과', '배', '수박']
columnsfruit = ['가격', '재고']
df_fruit = pd.DataFrame(fruit, index=indexfruit, columns=columnsfruit)
print(df_fruit)

# 문제2
score_data = {
    '이름':['지민','민수','수지','다현'],
    '수학':[85,90,78,92],
    '과학':[88,76,95,89],
    '파이썬':[100,100,90,100]
}

df_score= pd.DataFrame(score_data)
print(df_score)



# 문제3
tabledata = {
    '연도' : [2015,2016,2016,2017,2017],
    '지사' : ['한국','한국','미국','한국','미국'],
    '고객 수':[200,250,450,300,500]
}

# 1. tabledata를 이용하되, 칼렴의 순서를 ['연도','고객 수','지사'] 순으로 재배치하여 df_final을 생성하시오
# 2. df_final의 인덱스를 숫자가 아닌 ['A', 'B', 'C', 'D', 'E']로 변경하여 출력하시오
# 3. df_final.values를 출력했을 대, 첫 번째 행의 데이터([2015, 200, '한국])가 정상적으로 출력되는지 확인하시오


df_final = pd.DataFrame(tabledata, columns=['연도', '고객 수', '지사'])
print(df_final)
df_final.index = ['A', 'B', 'C', 'D', 'E']
print(df_final)
print(df_final.values[0])


