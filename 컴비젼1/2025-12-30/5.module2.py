# 1. random 모듈
# 난수 생성에 특화된 모듈

import random
print(random.randint(1, 10))

# 2. random 함수
# 0 이상 1미만 범위에서 임의의 실수를 생성
print(random.random())

# 50% 확률로 '안녕하세요 출력'

if random.random() < 0.5:
    print('안녕하세요') # random.random은 두번 호출됨


# 3. time 모듈
import time

# sleep() 함수
# 인수로 전달된 초 second 만큼 시스템을 일시 정지
# time.sleep(3)
print('hi')

# 4. datetime 모듈
# 날짜와 시간 데이터를 처리할 때 사용
print()
import datetime

# 1) now 메소드
# 시스템의 현재 날짜와 시간을 반환
present = datetime.datetime.now()
print(present)

# 2) date()함수
# 특정 날짜를 반환
birthday = datetime.datetime(2025, 12, 30)
print(birthday)

