# 정수 int

# int()함수를 이용하면 다른 자료형의 값을 정수형 데이터로 변환할 수 있다.
print(int(1.9)) # 1.9의 소수점이하를 제거
print(int(True)) # True는 1로 변환
print(int(False)) # False는 0으로 변환
print(int('100')) # 100 / 문자열 '100'을 정수 100으로 변환
print(type(int('100'))) # <class 'int'>

# 10진수를 2진수, 8진수, 16진수로  변환하는 방법
print()
n=95
print(type(n)) # <class 'int'?
print(bin(n)) # 2진수로 변환
print(oct(n)) # 8진수로 변환
print(hex(n)) # 16진수로 변환