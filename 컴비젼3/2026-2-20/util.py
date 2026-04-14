import pandas as pd
def change_csv_file_first_line_value(old_file_name, new_file_name):
    with open(old_file_name, encoding='utf-8') as f:
        # 전체 데이터를 읽어서 한 줄식 lines 리스트의 각 요소에 할당
        lines = f.read().splitlines()
        # 첫째 줄의 내용을 변경할 열 이름을 지정해서 변경
        lines[0] = '고유번호,제목,url,부서레벨1,부서레벨2,부서레벨3,부서레벨4,부서레벨5,집행년도,집행월,예산,집행,구분,부서명,집행일시,집행장소,집행목적,대상인원,결제방법,집행금액'
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

# 데이터를 읽어서 DataFrame으로 변환
def get_expense_data():
    # 3년치 데이터 파일을 DataFrame 형식으로 가져와 하나로 통합
    data_folder = './data/seoul_expense/'
    years = [2017, 2018, 2019]

    df_expense_all = pd.DataFrame()

    for year in years:
        expense_list_year_dir = data_foler + str(year) + '/'
        expense_list_tidy_file = f'{year}_expense_list_tidy.csv'

        path_file_name = expense_list_year_dir + expense_list_tidy_file

        df_expense = pd.read_csv(path_file_name)
        df_expense_all = pd.concat([df_expense_all, df_expense], ignore_index=True)
    return df_expense_all
