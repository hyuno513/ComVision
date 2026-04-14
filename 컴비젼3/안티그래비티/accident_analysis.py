import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import glob
import os

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

def main():
    # 1. 파일 찾기
    csv_files = glob.glob('*.csv')
    if not csv_files:
        print("CSV file not found.")
        return

    file_path = csv_files[0]
    print(f"Reading file: {file_path}")

    # 2. 데이터 읽기
    try:
        df = pd.read_csv(file_path, encoding='cp949')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file_path, encoding='euc-kr')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='utf-8')

    # 3. 데이터 전처리
    if '사고유형' in df.columns and '사고건수' in df.columns:
        stats = df.groupby('사고유형')['사고건수'].sum().sort_values(ascending=False)
    else:
        print("Required columns not found.")
        return

    # 4. 0~1% 등 작은 비율을 '기타'로 묶기 (가시성 개선)
    total = stats.sum()
    threshold = 0.02  # 2% 미만은 기타로 분류
    
    main_stats = stats[stats / total >= threshold]
    small_stats = stats[stats / total < threshold]
    
    if not small_stats.empty:
        others_sum = small_stats.sum()
        # '기타' 항목 추가
        main_stats['기타'] = others_sum

    # 데이터 준비
    labels = main_stats.index
    sizes = main_stats.values

    # 5. 시각화 개선
    plt.figure(figsize=(14, 10))

    # 색상 설정 (가시성이 좋은 색상 팔레트 사용)
    # tab20은 명확하게 구분되는 색상이 많음
    colors = plt.cm.tab20.colors
    # 데이터 개수에 맞춰 색상 리스트 슬라이싱 (부족하면 반복)
    if len(sizes) > len(colors):
        colors = colors * (len(sizes) // len(colors) + 1)
    colors = colors[:len(sizes)]

    # 파이 차트 그리기
    # explode: 가장 큰 비율 1~2개를 살짝 떼어내서 강조
    explode = [0.05 if i < 2 else 0 for i in range(len(sizes))]

    wedges, texts, autotexts = plt.pie(sizes, 
                                       labels=labels, 
                                       autopct='%1.1f%%', 
                                       startangle=140,
                                       colors=colors,
                                       explode=explode,
                                       shadow=True, # 입체감 추가
                                       pctdistance=0.85, # 퍼센트 텍스트 위치
                                       textprops={'fontsize': 12}) # 텍스트 크기 키움

    # 퍼센트 텍스트 스타일 개선
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')

    plt.title('사고 유형별 교통사고 통계', fontsize=20, pad=20)
    plt.axis('equal') 

    # 범례 추가 (오른쪽에 배치하여 차트 공간 확보)
    plt.legend(wedges, labels,
              title="사고 유형",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    output_file = 'accident_type_pie_stats_improved.png'
    plt.tight_layout() # 레이아웃 자동 조정
    plt.savefig(output_file, dpi=300)
    print(f"Improved graph saved to {output_file}")
    # plt.show()

if __name__ == "__main__":
    main()
