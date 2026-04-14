# continue 문
# 반복문의 시작 지점으로 제어의 흐름을 옮기는 역할
# 반복에서 제외하거나 생략하고 싶은 코드가 존재할때 사용

# 1에서 100까지의 모든 정수를 합하는데 3의 배수는 제외한 숫자들의 합

a = 0
s = 0
while a <= 99:

    a += 1
    if a % 3 != 0:
        s += a
    else:
        s += 0
print(s)

total = 0
for i in range(1, 101):
    if i % 3 == 0:
        continue
    total += i
print(total)


fruits = ['사과', '귤']
count = 3 # 입력 가능한 횟수

while count > 0:
    fruit = input("어떤 과일을 저장할까요? >>")
    if fruit in fruits: # fruits 리스트에 fuirt 변수에 값이 있다면
        print('동일한 과일이 있습니다.')
        continue
    fruits.append(fruit)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')

print(f'5개 과일은 {fruits}입니다.')


# 문제
x = 10000
print(f'현재 {x}원이 있습니다.')
while x > 0:
    y = int(input('사용할 금액 입력>>'))
    if y > x:
        print(f'{y-x}원이 부족합니다.')
        continue
    else:
        print(f'현재 {x-y}원이 있습니다.')
        x = x-y