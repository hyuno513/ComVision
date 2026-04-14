# format() 메소드
# format() 메소드의 인수로 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호{}로 표시하는 방식

print('My name is {}'.format('James'))
print('My name is {name}'.format(name='James')) # 변수명 지정 가능

names = 'James'
print('My name is {name}'.format(name=name))
