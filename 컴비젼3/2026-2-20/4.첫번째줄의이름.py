# 첫 번째 줄의 이름과 개수 변경

# 알아보기 어려운 열 이름은 한글로 변경
# 같은 파일 이름에 덮어써도 되지만 원본을 남겨두기 위해 다른 이름의 파일로 저장

def change_csv_file_first_line_value(old_file_name, new_file_name):
    with open(old_file_name, encoding='utf-8') as f:
        # 전체 데이터를 읽어서 한 줄식 lines 리스트의 각 요소에 할당
        lines = f.read().splitlines()
        print(lines[0])
        # 첫째 줄의 내용을 변경할 열 이름을 지정해서 변경
        lines[0] = '고유번호,제목,url,부서레벨1,부서레벨2,부서레벨3,부서레벨4,부서레벨5,집행년도,집행월,예산,집행,구분,부서명,집행일시,집행장소,집행목적,대상인원,결제방법,집행금액'
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

# 기존의 파일
old_file_name = './data/seoul_expense/2017/201702_expense_list.csv'

# 새로운 파일
new_file_name = './data/seoul_expense/2017/201702_expense_list_new.csv'

# 첫째 줄의 내용을 변경한 새로운 파일 생성
change_csv_file_first_line_value(old_file_name, new_file_name)

# 변경된 데이터 파일에서 첫 세줄을 읽어와 출력
with open(new_file_name, encoding='utf-8') as f:
    for k in range(3):
        print(f.readlines())


