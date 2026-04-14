import csv

file_path = '../2026-1-20/input/한국교육과정평가원_대학수학능력시험 연도별 응시현황_20251231.csv'

with open(file_path, mode='r', encoding='cp949') as f:
    reader = csv.reader(f)
    header = next(reader)  # 헤더(컬럼명) 건너뛰기

    for row in reader:
        if row:  # 데이터가 있는 줄만 처리
            # 데이터를 딕셔너리 형태로 구조화
            data_dict = {
                'year': row[0],
                'apply': int(row[2]),
                'attend': int(row[3]),
                'rate': row[4]
            }

            # 출력
            print(f"[{data_dict['year']}학년도] 지원: {data_dict['apply']:,}명, 응시율: {data_dict['rate']}%")