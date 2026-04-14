# 문자열 str
# 문자열 자료형, 기본적으로 따옴표로 묶어서 데이터를 표현
# 문자열을 한 글자이거나 여러 글자여도 작은 따음표'와 큰따옴표"를 모두 사용할 수 있음
# 각 따옴표를 3개씩 사용하는 삼중 따옴표(''' ''', """ """)도 사용할 수 있음
# single Line: 한 줄의 문자열: 작음 따옴표' 와 큰따옴표"
# multiple line: 여러줄의 문자열: 삼중따옴표(''' '''. """ """)

# 문자열 변환
# str() 함수를 사용하면 다른 자료형의 값을 문자열 데이터로 변환할 수 있음
print(str(100)) # 100
print(str(True)) # True
print(str(False)) # False
print(str(3.14)) # 3.14

# 문자열 인덱싱 indexing
# 0번부터 시작
s = 'hello'
print(s[1]) # e
# 마이너스(-)인덱스는 문자열 뒤에서부터 부여, 마지막 인덱스는 -1
print(s[-4]) # e
print(s[1] == s[-4]) #True
print(s[-5]) #h
print(s[0]) #h

# 문자열 슬라이싱 slicing
# 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용
# s[start:stop:step]
# start: 시작인덱스를 지정, 생략하면 끝까지 추출
# stop : 종료 인덱스를 지정, 생략하면 끝까지 추출
# step: 인덱스의 증감값, 생략하면 1씩 변화
print()
s='banana'
print(s[0:3]) # ban / 종류 인덱스는 포함 X
print(s[0:6:2]) # bnn
print(s[0:6:3]) # ba


