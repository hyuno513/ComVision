import pandas as pd
import matplotlib.pyplot as plt
import os

# Set font for Korean support on Windows
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

file_path = '한국도로교통공단_사고유형별 교통사고 통계_20241231.csv'

# Try reading with different encodings
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='euc-kr')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='utf-8')

# Check the columns
print("Columns:", df.columns)

# We want '사고 유형별' (By Accident Type).
# Based on common structures, we likely have '사고유형' or '사고유형대분류'.
# Let's inspect unique values to pick the best grouping column if '사고유형' is too granular.
# However, the user specifically asked for "사고 유형" (Accident Type).
target_column = '사고유형'
if target_column not in df.columns:
    # Fallback if specific column not found, though we saw it in previous step.
    # We saw: 사고유형대분류,사고유형중분류,사고유형
    target_column = df.columns[2] # Likely the 3rd one if naming varies

# Aggregating data - Summing up '사고건수' (Accident Count) by '사고유형'
# If there are duplicates for same type (unlikely in this stats file, but possible if split by other regions), we sum.
grouped_df = df.groupby(target_column)['사고건수'].sum()

# Plotting
plt.figure(figsize=(10, 8))
plt.pie(grouped_df, labels=grouped_df.index, autopct='%1.1f%%', startangle=140)
plt.title('사고 유형별 교통사고 통계')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

output_file = 'accident_type_pie_chart.png'
plt.savefig(output_file)
print(f"Pie chart saved to {output_file}")
plt.show()
