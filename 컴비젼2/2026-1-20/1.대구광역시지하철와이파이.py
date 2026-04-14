# 1. 각 호선별 와이파이 총 대수
# 2. 대합실 총 와이파이 대수
# 3. 대합실 + 승강장 각 통신사별 와이파이 대수

import csv
example_file = open('../2026-1-20/input/대구교통공사_와이파이 설치현황_20250930.csv')
example_dict_reader = csv.DictReader(example_file)
# print(example_dict_reader)
# for row in example_dict_reader:
#     print(row["호선"], row["대합실(SK)"])
#
# for row in example_dict_reader:
#         if row["호선"] == "01":
#             print(row["호선"], row["대합실(SK)"])

line_total = {}
concourse_total = 0
provider_total = {'SK':0, 'KT':0, 'LGU':0}

a = 0
b = 0
for row in example_dict_reader:
    line = row['호선']
    sk_c = int(row['대합실(SK)'])
    kt_c = int(row['대합실(KT)'])
    lgu_c = int(row['대합실(LGU플러스)'])
    sk_p = int(row['승강장(SK)'])
    kt_p = int(row['승강장(KT)'])
    lgu_p = int(row['승강장(LGU플러스)'])

    # 한 줄의 총합 계산
    row_sum = sk_c + kt_c + lgu_c + sk_p + kt_p + lgu_p
    print(row_sum)


    # 승강장의 총 와이파이 대수
    a += (sk_p + kt_p + lgu_p)
    # 대합실의 총 와이파이 대수
    b += (sk_c + kt_c + lgu_c)
    # 각 호선별 와이파이 총 대수 합산
    if line not in line_total:
        line_total[line] = 0
    line_total[line] += row_sum



    # 통신사별 와이파이 대수 합산(대합실 + 승강장)
    provider_total['SK'] += (sk_c + sk_p)
    provider_total['KT'] += (kt_c + kt_p)
    provider_total['LGU'] += (lgu_c + lgu_p)

print('각 호선별 와이파이 총 대수')
for line, total in sorted(line_total.items()):
    print(f'{line}호선 : {total}대')


print(f'승강장의 총 와이파이 대수는{a}입니다.')
print(f'대합실의 총 와이파이 대수는{b}입니다.')

print('통신사별 와이파이 총 대수')
for provider, total in provider_total.items():
    print(f'{provider}: {total}대')
