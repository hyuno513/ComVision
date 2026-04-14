# break 문
# while 문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문
# 반복문 내에 break문이 나타나면 곧바로 break문이 포함된 반복문은 종료

n=1
while n <= 10:
    print(n)
    n += 1
print(n) # 11

n=1
while True:
    print(n)
    if n == 10:
        break
    n += 1
print(n) # 10


while True: # 무한루프
    city = input('대한민국의 수도는 어디인가요? >>')
    city = city.strip() # strip()은 공백문자 제거
    if city == '서울' or city =='seoul' or city = 'SEOUL':
        print('정답')
        break
    else:
        print('오답. 다시 시도')

