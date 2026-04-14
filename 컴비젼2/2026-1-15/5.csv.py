# csv
# csv단점
# 값에 유형이 없음 모든 것은 다 문자열
# 글꼴 크기나 색상을 설정할 수 없음
# 여러 개의 워크시트를 가질 수 없음
# 셀의 너비나 높이를 지정할 수 없음
# 셀을 병합할 수 없음
# 그림이나 차트를 포함할 수 없음

# csv 장점
# 단순함
# 많은 프로그램에서 지원을 하고 텍스트 편집기에서 볼 수 있으며
# 스프레드 시트 데이터를 표현하는 간단한 방법

# 주의점
# 텍스트로 구성이 되어 있어서 각줄에 대해 split(',')을 호출하여 쉼표로 구분된 값에서 문자열 리스트를 얻을 수 있음
# 그러나 csv 파일의 모든 쉼표가 두 셀의 경계를 나타내지 않고, 값의 일부인 경우도 있음
# 이런 잠재적인 문제 때문에 csv 파일을 읽거나 슬대 csv 모듈을 사용하는 것이 좋음

# 1. reader 객체
# csv 모듈은 별도의 설치없이 사용가능
import csv

# csv 모듈을 사용해서 csv 파일을 읽으려면 다른 텍스트 파일처럼 open()함수로 파일을 열어야함

example_file = open('../2026-1-15/input/example.csv')
print(example_file.read())

# read() 대신 csv.reader() 함수에 전달, reader()객체를 반환
example_reader = csv.reader(example_file)

# list로 변환해서 값에 접근
print(example_reader) # 주소값
example_data = list(example_reader)
print(example_data) # ?? 안됨??
# print(example_data[0][1])

# 2. for 반복문을 활용해 reader 객체로부터 데이터 읽기
# csv 파일이 큰 경우에넌  전체 파일을 한번에 메모리에 로드하지 않고
# for 반복문에서 reader 객체 사용
# reader 객체는 한번만 사용가능하기 대문에 다시 사용할려면 새로 reader 객체 생성

example_file = open('../2026-1-15/input/example.csv')
example_reader = csv.reader(example_file)
for row in example_reader:
    # 각 행의 번호를 얻으려면 reader 객체의 line_num 변수를 사용
    print(f'Row #{str(example_reader.line_num)}{row}{row[0]}')

# 3. csv 객체의 DictReader 와 DictWriter
# 헤더 행이 있는 csv 파일의 경우 reader나 writer 객체보다 DictReader나 dicWriter 객체를 사용하는 것이 작업하기 편함

example_file = open('../2026-1-15/input/example_with_header.csv')
example_dict_reader = csv.DictReader(example_file)
# DictReader는 객체의 row를 딕셔너리 객체로 설정하고, 첫번째 행에 있는 정보를 건너뜀
for row in example_dict_reader:
    print(f'{row["Timestamp"]},{row["Fruit"]}, {row["Quantity"]}')

# DicWriter 객체는 csv 파일을 생성하기 위해 딕셔너리를 사용
output_file = open('../2026-1-15/output/output_with_header.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file,['Name', 'Pet', 'Phone'])
# 파일에 헤더 행을 넣고 싶으면 writeheader()를 호출
output_dict_writer.writeheader()
# writerow() 메서드를 호출해서 각 행을 쓸 수 있는데 이 대 딕셔너리를 사용
# 딕셔너리의 키는 헤더이고, 딕셔너리의 값은 파일에 쓰려는 데이터가 들어감
output_dict_writer.writerow({'Name':'Alice', 'Pet':'cat', 'Phone':'555-1234'})
output_dict_writer.writerow({'Name':'Bob', 'Phone':'555-9999'}) # 없는부분은 없는대로
output_dict_writer.writerow({ 'Phone':'555-5555', 'Name':'David', 'Pet':'dog'}) # 오류나지 않음
output_file.close()