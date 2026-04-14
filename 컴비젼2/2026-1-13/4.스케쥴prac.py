# 오늘의 스케줄을 입력하면 그 내용이 모두 파일이 보관되는 프로그램
# 스케줄을 입력하지 않고 enter를 누르면 프로그램을 종료
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt
# '2020-10-22.txt'와 같은 형식을 갖추고 있다
# 폴더는 output파일

import datetime
print(datetime.date.today())

filename = f'./output/{datetime.date.today()}.txt'

print('입력 없이 Enter 누르면 종료됩니다.')

with open(filename,'at', encoding='utf-8') as file:
    while True:
        schedule = input('오늘의 스케줄을 입력하세요>>')
        if not schedule:
            break
        file.write(schedule + "\n")