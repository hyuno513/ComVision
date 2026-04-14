# 새로 생성된 파일의 개수 확인

import glob

data_folder = './data/seoul_expense/'

years = [2017, 2018, 2019]

for year in years:
    path_name = data_folder + str(year)
    print('[폴더 이름]', path_name)

    new_csv_files = []

    # 지정된 폴더에서 파일명에서 _new.csv가 포함된 파일만 지정
    file_name_for_glob = path_name + './*_new.csv'

    for new_csv_file in glob.glob(file_name_for_glob):
        # 반환값에서 폴더는 제거하고 파일 이름만 추출
        new_csv_files.append(new_csv_file.split('\\')[-1])
        print(new_csv_file)

print('[파일 개수]', len(new_csv_files))
print('* 새롭게 생성된 csv 파일:', new_csv_files)
