# 리스트 list
# 여러 값을 저장할 때 가장 많이 사용하는 자료형
# 저장하고자 하는 값들의 자료형(type)이 서로 다르더라도 하나의 리스트에 저장

# 대괄호[] 또는 list()함수를 이용
# 정수, 실수, 문자열 각 1개씩 저장하고 있는 리스트 생성
li=[100, 3.14, 'hello']
print(li) # [100, 3.14, 'hello']
print(type(li)) # <class 'list'>

# 인덱싱
# 문자열과 동일한 방식으로 인덱싱을 지원
# 저장된 요소들마다 고유번호와 인덱스를 부여하여 순서대로 관리
print()
print(li[0]) # 100
print(li[1]) # 3.14
print(li[2]) # 'hello'

# 슬라이싱
print()
li=[10,20,30,40]
print(li[0:3]) # [10,20,30]
print(li[:2]) # [10, 20]
print(li[::2]) # [10,30]

# 요소의 추가와 삭제
# 새로운 요소를 추가할 때는 append()와 insert() 매소드를 사용
# append(): 항상 마지막 요소로 추가
# insert(): 추가할 인덱스(위치 정보)를 지정
print()
scores = [50,40,30]
scores.append(100)
print(scores) # [50, 40, 30, 100]
print(scores[1]) # 40
scores.insert(0,90)
print(scores)
print(scores[1]) # 50

# pop() : 인덱스를 전달하지 않으면 마지막 요소를 삭제
# 인덱스를 전달하면 전달된 인덱스의 요소를 삭제
scores.pop()
print(scores)
scores.pop(2)
print(scores) # [90, 50, 30]