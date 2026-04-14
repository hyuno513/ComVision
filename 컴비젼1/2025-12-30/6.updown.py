import random
from datetime import *

one = random.randint(1,100)
print(one)
print('updown 게임을 시작합니다.')
start = datetime.now()

while True:
    a = int(input('어떤값일까요>>'))
    if a == one:
        end = datetime.now()
        elapse = end - start
        elapse = elpase.total_seconds()
        print(f'정답입니다. 걸린 시간{elapse}')
        print('시스템을 종료')
        break
    else:
        if a > one:
            print('오답 다시입력해주세요.')
            print('다운')
        else:
            print('오답 다시입력해주세요.')
            print('업')