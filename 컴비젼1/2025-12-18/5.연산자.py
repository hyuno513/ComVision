# 산술연살자
a = 7
b = 2
print(f'{a}/{b}={a / b}') # 나눗셈
print(f'{a}//{b}={a //b}') # 몫
print(f'{a}%{b}={a % b}') # 나머지

# 대입연산자
a , b =10, 20
print(f'a={a}, b={b} = {a , b}')
a, b = b, a # 값을 교환
print(f'a={a}, b={b} = {a , b}')

###
# 문제: 출력 결과를 보고 코딩하시오.
piggy_bank = 1000

money = 10000
snack = 2000
# 출력결과
# 저금통에 용돈 10000원을 넣었습니다.
# 지금 저금통에는 11000원이 있습니다.
# 저금통에서 스낵 구입비 2000원을 뺐습니다.
# 지금 저금통에는 9000원이 있습니다.

# piggy_bank = piggy_bank + money
piggy_bank += money
piggy_bank -= snack

print(f'저금통에 용돈 {money}원을 넣었습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')
print(f'저금통에서 스낵 구입비 {snack}원을 뺐습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')

###
# 비교연산자
# 결과 값을 True와 False 둘 중 하나
print(f'{a} > 10: {a > 10}') # True a가 10보다 크다.
print(f'{a} == 10: {a == 10}') # False a가 10이 같다.
print(f'{a} != 10: {a != 10}') # True a와 10이 다르다.

# 논리연산자: and &, or ||
# 논리곱
print(f'True and True: {True and True}') # True
print(f'True and False: {True and False}') # False
print(f'False and False: {False and False}') # False
print()

# 논리합
print(f'True or True: {True or True}') # True
print(f'True or False: {True or False}') # True
print(f'False or False: {False or False}') # False

# not a : a가 참(True)
a = 10
b = 0
c = -10

print(f'{a} > 0 and {b} > 0: {a > 0 and b > 0}') # False
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}') # True
print(f'not {a} : {a, not a}')
print(f'not {b} : {b, not b}')

# 프로그래밍에서 0을 제외한 나머지 숫자는 무조건 True 로 인식
print(not a)
print(not b)
print(not c)
print(not False)


print('=' * 10)
# 시퀀스 연산자: 순서가 있는 시퀀스 (리스트, 튜플, range, 문자열 등)에서 사용할 수 있는 연산자
# + : 연결하기
# * : 반복하기
tree = '#'
space = ' '
print(space * 4 + tree * 1)
print(space * 3 + tree * 3)
print(space * 2 + tree * 5)
print(space * 1 + tree * 7)
print(space * 0 + tree * 9)

# 삼항 조건 연산자
# 일반적인 삼항 조건 연산자: 조건식 ? 참 : 거짓
# 파이썬 삼항 조건 연산자: 참 if 조건식 else 거짓

a = 10
b = 20
result = (a-b) if (a>=b) else (b-a) # 조건식 a>=b 은 False, b-a 실행
