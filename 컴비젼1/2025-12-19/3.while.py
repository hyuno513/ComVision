# while 문
# 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용
# while 조건식:
# 반복실행문

n = 1
while n <= 10:
    print(n)
    n += 1

# while문의 중첩
# while문 내부에 또 다른 while문이 나타나는 것

day = 1
hour = 1
while day <= 5:
    hour = 1
    while hour <= 3:
        print(f'{day}일차 {hour}교시 입니다.')
        hour += 1
    day += 1

# 100부터 50 사이의 짝수를 출력
n = 100
while n >= 50:
    print(n)
    n -= 2

while n >= 50:
    if n % 2 == 0:
        print(n)
    n-= 1

## 구구단 2단부터 9단까지 출력
# 각 단 앞이 제목, 마지막에 구분선을 넣음
# 2끝났습니다.
# 3단 시작

x = 2
while x <= 9:
    y = 1
    print(f'{x}단 시작')
    while y <= 9:
        print(f'{x}x{y} = {x * y}')
        y += 1
    print(f'{x}단이 끝났습니다.')

    x = x + 1


# 1~100 출력
# a = 1
# while a <= 100:
#     b=0
#     L = [a]
#     while b <= 9:
#         L.append(a+b)
#         print(L)
#     a += 10

a = 1
while a <= 100:
    if a % 10 -1 == 0: # 이해해오기
        print()
    print(f'{a}   ', end=' ')
    a += 1
