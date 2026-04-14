# 데이터 처리

# 데이터 정제와 정리 과정이 필요
# 데이터를 살표보면 일부 데이터 값이 누락되있거나 부정확한 값이 들어가 있는 경우
# 자신이 직접 설계해서 만든 데이터가 아니고 외부에서 데이터를 가져온 경우 데이터가 원하는 구조가 아닐 수 있음

# 1) 수집된 데이터 파일의 구조 분석
data_file = './data/seoul_expense/2017/201701_expense_list.csv'

# 첫 세줄 출력
with open(data_file, encoding='utf-8') as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

    print(line1)
    print(line2)
    print(line3)

# 각 줄에 있는 데이터의 개수를 확인
line1_len = len(line1.split(','))
line2_len = len(line2.split(','))
line3_len = len(line3.split(','))

print('[각 줄의 데이터값의 개수]')
print(f'첫째 줄:{line1_len}, 둘째 줄:{line2_len}, 셋째 줄:{line3_len}')

# 전체 줄의 데이터 개수 확인
# with open(data_file, encoding='utf-8') as file:
#     cnt = 1
#     while True:
#         str = file.readline()
#         if str == '':
#             break
#         lines = len(str.split(","))
#         if lines != 20: # 개수가 20개가 아닌 경우
#             print(f'{cnt}줄의 개수: {lines}')
#         cnt += 1

# 다음은 문자열에서 따옴표 안에 있는 콤마를 제거하고 콤마를 기준으로 값의 개수를 세는 함수
def get_value_count(line):
    line_rep_list = list()
    for k, x in enumerate(line.split('"')):
        if k % 2 != 0:
            x = x.replace(',', '')
        line_rep_list.append(x)

    line_rep_str = ''.join(line_rep_list)
    return len(line_rep_str.split(','))

print("[각 줄의 데이터값의 개수 : 함수 적용]")
# 전체 줄의 데이터 개수 확인
with open(data_file, encoding='utf-8') as file:
    cnt = 1
    while True:
        str = file.readline()
        if str == '':
            break
        lines = get_value_count(str)
        if lines != 20: # 개수가 20개가 아닌 경우
            print(f'{cnt}줄의 개수: {lines}')
        cnt += 1