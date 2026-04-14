# 1) 날짜 자동생성: data_range
# 입력해야 할 날짜가 많으면 pandas에서 날짜를 자동생성하는 date_range() 사용
# 몇 가지 설정만 하면 원하는 날짜를 자동으로 생성하므로 날짜 데이터를 입력할 때 편리

# pd.date_range(start=None, end=None, periods=None, freq='D')
# start는 시작날짜
# end는 끝날짜
# periods는 날짜 데이터 생성 기간
# freq는 날짜 데이터 생성 주기
# start는 필수이고, end나 periods는 둘 중 하나만 있어도 됨
# freq는 입력하지 않으면 'D' 옵션이 설정돼 달력날짜 기준으로 하루씩 증가

import pandas as pd
print(pd.date_range(start='2026-01-01', end='2026-02-10'))

# 날짜 데이터를 입력할때 yyyy-mm-dd 형식이 아니라
# yyyy/mm/dd, yyyy.mm.dd, mm-dd-yyyy, mm/dd/yyyy, mm.dd.yyyy 같은 형식도 사용가능하고
# 대신 출력은 yyyy-mm-dd 형식으로 생성
print(pd.date_range(start='2026/01/01', end='2026.01.07'))

# 끝 날짜를 지정하지 않고 periods만 입력해서 날짜 생성
print(pd.date_range(start='01-01-2026', periods=7))

# * pandas date_range() 함수의 freq 옵션

# 약어 설명 사용 예
# D : 달력 날짜 기준 하루 주기 ex) 하루 주기: freq = 'D', 이름 주기: freq = '2D'
# B : 업무 날짜 기준 하루 주기 ex) 업무일(월~금) 기준으로 생성, freq = 'B', freq='38'
# W : 일요일 시각 기준 일주일 주기 ex) 월요일 : W-MON, 화요일 W-TUE

# 2일씩 증가하는 날짜를 생성
print(pd.date_range(start='01-01-2026', periods=4, freq='2D'))

# 달력의 요일을 기준으로 일주일씩 증가하는 날짜를 생성
print(pd.date_range(start='01-01-2026', periods=4, freq='W'))

# 업무일 기준 2개월 월말 주기로 12개 날짜를 생성
print(pd.date_range(start='01-01-2026', periods=12, freq='BME'))

# 분기 시작일을 기준으로 4개의 날짜를 생성
print(pd.date_range(start='01-01-2026', periods=4, freq='QS')) # QS: 분기

# 연도의 첫날을 기준으로 1년 주기로 3개의 날짜를 생성
print(pd.date_range(start='01-01-2026', periods=3, freq='YS'))


# 날짜뿐 아니라 시간을 생성하는 방법
# 1시간 주기로 10개의 시간을 생성한 예
print(pd.date_range(start='01-01-2026 08:00', periods=10, freq='h'))

# 업무 시간을 기준으로 1시간 주기로 10개의 시간을 생성하는 예
# 업무 시간은 9시부터 17시까지이므로 start시간을 9시 이전으로 설정해도 9시부터 표시
print(pd.date_range(start='01-01-2026 08:00', periods=10, freq='30min'))

# 30분 단위로 4개의 시간을 생성한 예
print(pd.date_range(start='01-01-2026 08:00', periods=4, freq='30min'))

# 10초 단위로 증가하면서 4개의 시간을 생성한 예
print(pd.date_range(start='01-01-2026 08:00', periods=4, freq='10s'))

# date_range()를 이용해 Series의 index를 지정한 예
index_date = pd.date_range(start='2026-02-01', periods=5, freq='D')
s = pd.Series([51,62,55,49,58], index=index_date)
print(s)

