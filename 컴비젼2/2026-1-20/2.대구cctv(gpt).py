import csv

file_path = '../2026-1-20/input/대구광역시_수성구_불법주정차단속CCTV_20250915.csv'
count = 0

# 파일을 읽기 모드로 열기
with open(file_path, mode='r', encoding='cp949') as f: # cp949 : 한글 인코딩
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        if row: # 빈 줄이 아니라면 카운트 증가
            if row[1] == '불법 주정차 단속용':
                count += 1

print(f'csv파일 내 불법 주정차 단속용 CCTV 설치 대수 {count}대')