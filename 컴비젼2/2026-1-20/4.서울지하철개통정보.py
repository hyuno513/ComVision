import csv

file_path = '../2026-1-20/input/서울교통공사_지하철개통정보_20241129.csv'

subway_list = []

with open(file_path, mode='r', encoding='cp949') as f:
    # DictReader를 사용하면 헤더를 Key로 바로 쓸 수 있습니다.
    reader = csv.DictReader(f)

    for row in reader:
        # 데이터 정제: 비어있는 값은 '0'이나 '정보없음'으로 처리
        item = {
            'no': row['연번'],
            'line': row['호선'],
            'section': row['구간'],
            'stations': row['역개수'] if row['역개수'] else "0",
            'length': row['연장(km)'] if row['연장(km)'] else "0.0",
            'date': row['개통일자']
        }
        subway_list.append(item)

# 데이터 출력 (for문 활용)
print(f"{'호선':<4} | {'구간':<20} | {'역개수':<4} | {'연장(km)':<6} | {'개통일'}")
print("-" * 70)

for s in subway_list:
    # 2호선 데이터만 필터링해서 보고 싶다면 아래 if문을 활성화하세요.
    # if s['line'] == '2':
    print(f"{s['line']:>4} | {s['section']:<20} | {s['stations']:>5} | {s['length']:>8} | {s['date']}")

# 간단한 통계 계산 예시
total_length = sum(float(s['length']) for s in subway_list)
print("-" * 70)
print(f"전체 개통 구간 연장 합계: {total_length:.2f} km")