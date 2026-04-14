import csv

file_path = '../2026-1-20/input/서울시설공단_서울월드컵경기장 주경기장 사용자 통계_20241130.csv'

stadium_data = []

# 1. 파일 읽기
with open(file_path, mode='r', encoding='cp949') as f:
    # DictReader는 따옴표(")로 묶인 데이터 안의 쉼표를 알아서 잘 처리해줍니다.
    reader = csv.DictReader(f)

    for row in reader:
        # 컬럼명에 공백이 섞여 있을 수 있으므로 strip()으로 정리된 딕셔너리 생성
        clean_row = {key.strip(): value.strip() for key, value in row.items()}
        stadium_data.append(clean_row)

# 2. 데이터 출력 및 간단한 분석
print(f"{'연번':<4} | {'구분':<6} | {'관람인원':<8} | {'행사내용'}")
print("-" * 80)

total_attendance = 0
max_revenue = 0
max_revenue_event = ""

for event in stadium_data:
    # 데이터 변환 (비어있는 값은 0으로 처리)
    try:
        attendance = int(event['관람인원(명)'] or 0)
        revenue = int(event['수입금(원)'] or 0)
    except ValueError:
        attendance = 0
        revenue = 0

    total_attendance += attendance

    # 가장 수입이 높았던 행사 찾기
    if revenue > max_revenue:
        max_revenue = revenue
        max_revenue_event = event['경기(행사) 내용']

    # K리그 경기만 골라서 출력해보기
    if event['구 분'] == 'K리그':
        print(f"{event['연번']:>4} | {event['구 분']:<6} | {attendance:>8,}명 | {event['경기(행사) 내용']}")

# 3. 요약 결과 출력
print("-" * 80)
print(f"▶ 총 누적 관람인원: {total_attendance:,}명")
print(f"▶ 최고 수입 행사: {max_revenue_event} ({max_revenue:,}원)")