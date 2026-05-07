# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import platform

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')

# CSV 파일 읽기
csv_path = 'input/한국철도공사_시군구단위 거주 철도이용객 이용 시간대별 소비업종 정보_20221115.csv'
df = pd.read_csv(csv_path, encoding='utf-8')

print("=" * 70)
print("한국철도공사 소비 데이터 분석 보고서")
print("=" * 70)
print(f"\n[1] 데이터 크기: {df.shape[0]:,}행 x {df.shape[1]}열")

print("\n[2] 컬럼 목록:")
for i, col in enumerate(df.columns):
    print(f"    {i:2d}. {col}")

print("\n[3] 결측치 확인:")
null_count = df.isnull().sum().sum()
print(f"    총 결측치: {null_count}개 (결측치 없음)" if null_count == 0 else f"    총 결측치: {null_count}개")

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"\n[4] 수치형 데이터 통계:")
print(df[numeric_cols].describe().to_string())

print(f"\n[5] 카테고리 데이터:")
print(f"    - 시도: {df['시도명'].nunique()}개 지역")
print(f"    - 시군구: {df['시군구명'].nunique()}개 지역")
print(f"    - 시간대 코드: {sorted(df['시간코드'].unique())}")
print(f"      (51: 오전~, 52: 오전~, 53: 낮~, 54: 오후~, 55: 저녁~)")

print(f"\n[6] 시간대별 평균 소비액:")
time_stats = df.groupby('시간코드')['전체_카드'].agg(['count', 'mean', 'min', 'max'])
print(time_stats.to_string())

print(f"\n[7] 시도별 평균 소비액 상위 10:")
province_mean = df.groupby('시도명')['전체_카드'].mean().sort_values(ascending=False).head(10)
for i, (prov, val) in enumerate(province_mean.items(), 1):
    print(f"    {i:2d}. {prov}: {val:,.0f}원")

print(f"\n[8] 상관계수 분석 (전체_카드와의 상관관계):")
corr = df[numeric_cols].corr()['전체_카드'].sort_values(ascending=False)
for col, val in corr.items():
    if col != '전체_카드':
        print(f"    {col:20s}: {val:7.4f}")

print(f"\n[9] 소비업종별 총액:")
spending_cols = [col for col in numeric_cols
                 if col not in ['전체_카드', '법정동시도코드', '법정동시군구코드', '시간코드']]
spending_sum = df[spending_cols].sum().sort_values(ascending=False)
for i, (col, val) in enumerate(spending_sum.items(), 1):
    pct = (val / df[spending_cols].sum().sum()) * 100
    print(f"    {i:2d}. {col:12s}: {val:15,.0f}원 ({pct:5.1f}%)")
