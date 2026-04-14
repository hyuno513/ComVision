import csv

file_path = '../2026-1-20/input/주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20251231.csv'

hakwon_data = []

with open(file_path, mode='r', encoding='cp949') as f:
    reader = csv.reader(f)
    header = next(reader)  # 헤더(컬럼명) 건너뛰기

    for row in reader:
        if row:  # 데이터가 있는 줄만 처리
            # 데이터를 딕셔너리 형태로 구조화
            data_dict = {
                '순번': int(row[0]),
                '학원 및 교습소명': row[1],
                '주소': row[2],
            }

            print(f"{data_dict['순번']}, {data_dict['학원 및 교습소명']},  {data_dict['주소']}")