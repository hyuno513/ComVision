# enumerate(): 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태로 함께 출력
# for item in enumerate([리스트]):
# 반복실행문

for item in enumerate(['가위', '바위', '보']):
    print(item)

# (0, '가위')
# (1, '바위')
# (2, '보')

# len() : 함수에 전달된 객체의 길이(항목수)를 반환
print()
li = ['a', 'b', 'c', 'd']
print(len(li))

d = {'a': 'apple', 'b': 'banana'}
print(len(d)) # 2

print(len(range(10))) # 10
print(len(range(1, 10))) # 9

# range함수와 리스트의 길이를 구하는 len함수를 함께 사용하면 리스트의 인덱스를 생성 가능
seasons= ['봄', '여름', '가을', '겨울']
seasons_eng = ['spring', 'summer', 'fall', 'winter']

for i in range(len(seasons)):
    print(f'{seasons[i]} / {seasons_eng[i]}')


# sorted(): 전달된 반복가능객체의 오름차순 정렬 결과를 반환
# reserve=True 옵션을 추가할 경우 내림차순 정렬 결과를 반환

print()
li = ['b', 'c', 'a', 'd']
print(sorted(li))

li2 = [6,3,1,2,5,4]
print(sorted(li2, reverse=True))