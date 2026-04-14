# 파이썬 내장 모듈인 glob을 이용해 지정한 폴더에 파일이 있는지 확인

import glob

path_name = './data/seoul_expense/2017' # 폴더이름

file_name_for_glob = path_name + '/*list.csv'
csv_files = list()

for csv_file in glob.glob(file_name_for_glob):
    # 반환값에서 폴더는 제거하고 파일 이름만 추출
    print(csv_file)
    csv_files.append(csv_file.split('\\')[-1])

print('[폴더 이름]', path_name)
print('[파일 개수]', len(csv_files))
print('* CSV파일: ', csv_files)