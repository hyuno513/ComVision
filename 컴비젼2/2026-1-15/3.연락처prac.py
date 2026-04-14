# 연락처.txt파일을 이용하여 파일에 저장된 연락처 중에서 전화번호가 011로 시작하는 모든 연락처를
# 010으로 수정

# 지시사항
# 연락처.txt 파일은 다음형식으로 저장
# "김나라", "목포시", "010-1111-1111"
# 실행 예
# 총 3건의 011 데이터를 찾았습니다.

# file = open('../2026-1-15/input/연락처.txt', 'rt')
# line_list = file.readlines()
#
# i = 0
# for line in line_list:
#     # print(line[15:18], end ='')
#     if line[15:18] == '011':
#         line[15:18] == '010'
#         i += 1
#
# file.close()
# print(f'총 {i}건의 011 데이터를 찾았습니다.')
count = 0
data_list_new =[]
with open('../2026-1-15/input/연락처.txt', 'rt') as file:
    data_list = file.readlines()

    for row in data_list:
        # print(row, end='')
        parts = row.split(',')
        print(parts)
        print(parts[2])
        if '"011-' in parts[2]:
            count += 1
            parts[2] = parts[2].replace('011', '010', 1)

        data_list_new.append(parts)
print(count)
for row in data_list_new:
    print(row)