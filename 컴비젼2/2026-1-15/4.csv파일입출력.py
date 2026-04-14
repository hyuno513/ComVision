# csv 파일 입출력

# 1. csv 파일이란?
# Comma Sepparated Values 의 약자로 '쉼표로 분리한 값들'
# 데이터베이스나 스프레드시트 데이터를 저장하기 위해서 사용하는 형식
# 내부는 실제 쉼표 (,)를 이용해서 모든 항목이 구분되어있으며
# 쉼표로 구성된 각 항목들이 테이블을 구성하는 각각의 데이터가 되는 방식
# 메모장에서는 텍스트로, 엑셀에서는 각 셀로 나누어서 보임

# 2. csv 파일 읽기
# csv 파일은 쉼표(,)로 데이터가 구분되어 있어서 문자열 처리 메소드를 활용하면
# 별도의 외부 모듈이 없어도 충분히 읽을 수 있음
# 1) 한 줄에 한 데이터가 있기 때문에 realine() 메소드로 한줄식 읽음
# 2) 쉼표(,)로 분리하기 위해서 split() 메소드를 이용

student_list = []
with open('../2026-1-15/input/학생명단.csv', 'rt') as file:
    file.readline() # 학번, 이름, 주소, 연락처
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        print(student)
        student_list.append(student)

print(student_list)

# 학생 1명의 정보인 학번, 이름, 주소, 연락처를 student 리스트에 저장하고,
# student_list 리스트에 student 리스트를 저장

# csv 파일을 사용하다 보면 간혹 큰 따옴표(")를 이용해서 텍스트를 묶는 경우가 있음
# 큰 따옴표를 제거하기 위해서 회원명에 추가로 strip() 메소드를 사용

member_list =[]
with open('../2026-1-15/input/회원명단.csv','rt') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"') # 큰따옴표 제거
        member_list.append(member)
print(member_list)

# member[0]에는 큰 다옴표가 포함된 회원명이 저장되어 있기 때문에 member[0].strip('"')d으로 큰 따옴표 제거

# 3. csv 모듈로 csv 파일 생성하기
# import csv를 통해서 csv 파일을 쉽게 처리할 수 있는 csv 모듈을 사용

# w 모드로 열고 생성된 파일 객체를 csv.writer() 메소드에 전달
# 그러면 csv 파일을 생성할 수 있는 객체가 생성되는데 이 객체를 이용해서
# writerow() 메소드를 호출하면 csv 파일에 데이터를 저장할 수 있음

import csv

with open('../2026-1-15/output/차량관리_01.csv', 'w') as file:
    csv_maker = csv.writer(file, delimiter=',') # delimeter: 구분기호
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])

print('차량관리_01.csv파일이 생성되었습니다.')

# 불필요한 라인이 하나식 추가되어 있는데 이를 막기위해서 새로운 라인을
# 추가하지 못하도록 newline옵션을 사용할 수 있음
# 줄 바꿈이 되지 않도록 newline 옵션에 빈 문자열을 지정하고 이를 코드에 반영

with open('../2026-1-15/output/차량관리_02.csv', 'w', newline='') as file:
    csv_maker = csv.writer(file, delimiter=',') # delimiter: 구분기호 delimeter 아님!
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])

# 4. csv 모듈로 csv 파일 읽기
# csv 파일을 읽기 위해서는 r모드로 파일을 열고 생성된 파일을 객체 csv.reader() 메소드에 전달
# csv.reader() 메소드는 csv 파일을 읽고 그 내용을 읽고 저장한 객체 iterator를 반환

with open('../2026-1-15/output/차량관리_02.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for line in csv_reader:
        print(line)

