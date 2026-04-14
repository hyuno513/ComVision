'''
변수 variable: 어떤 데이터를 저장하고자 할때 사용하는 메모리 저장소

변수명 생성 규칙
1. 영문, 한글, 숫자, 언더바(_)로 구성
2. 특수문자 사용X
3. 대소문자 구분이 가능 예 number와 Number는 다른 변수로 취급
4. 변수명의 첫글자는 숫자 사용 X, my2002(0), 2002my(X)
5. 키워드(list, dict, if, for, and 등)은 사용X

권장하는 변수명
1. 가급적 영문 소문자로 작성
2. 한글은 사용하지 않고 영어 변수명 사용
3. 변수명으로 저장된 데이터 유추가 가능하도록 사용

'''
# 자동완성 단축키: Tab


# 변수가 필요한 이유
print('Hello Python!')
print()
# 윗 줄에 print() 한 문자열을 다시 사용하고 싶은 경우
# 2번째 줄에 사용한 문자열은 줄 바꿈을 하면 메모리에서 지워져서
# 3번째 줄에서는 다시 사용할 수 없다.

# print(__doc__)은 ''' '''에서만 사용이 가능하며 #에서 쓰일 경우 None으로 나오게 된다.
print(__doc__)

# 만약 문자열을 줄바꿈을 해서도 사용을 하려면
# 프로그램에게 줄바꿈을 하더라도 사용하가능하게 메모리에 저장하게 명령해야 한다.

# str = 'Hello Python!'
# print(str)
# print()
# print(str)

# 위의 경우 문자열을 변수를 사용해서 메모리에 저장을 해서
# 34번째줄, 36번째줄 모두 사용이 가능한 상태

name = 'Alice'
age = 25
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호''' # multiple line 문자열 저장
boyfriend = None # 아무값도 저장하지 않음, 다른 언어에서는 Null로 표현
height = 168.5 # 실수를 저장

print(name)
print(age)
print(address)
print(boyfriend)
print(height)


