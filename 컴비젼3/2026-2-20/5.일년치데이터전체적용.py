# 1년치 데이터 전체에 적용할 수 있도록 함수를 만듬

import util
import os

data_folder = './data/seoul_expense/'

years = [2017, 2018, 2019]

def change_year_csv_file_first_line_value(year, data_folder):
    expense_list_year_dir = data_folder + str(year) +'/'
    extension = 'csv'
    for k in range(12):
        old_file_name = expense_list_year_dir + f'{year}{k + 1:02d}_expense_list.{extension}'
        new_file_name = expense_list_year_dir + f'{year}{k + 1:02d}_expense_list_new.{extension}'
        util.change_csv_file_first_line_value(old_file_name, new_file_name)


for year in years:
    print(f'{year}년 데이터의 첫 번재 줄의 열 이름을 변경해서 새 파일에 저장합니다.')
    change_year_csv_file_first_line_value(year, data_folder)

print('모든 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일로 저장했습니다.')