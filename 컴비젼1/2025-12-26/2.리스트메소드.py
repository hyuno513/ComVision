# 2. 리스트 메소드
# 1) append()
# 리스트의 끝에 인수로 전달된 데이터를 추가

mylist = ['apple', 'banana']
mylist.append('cherry')
print(mylist)

# 2) extend()
print()
mylist = ['apple', 'banana']
mylist.extend(['cherry','mango'])

mylist = ['apple', 'banana']
mylist += ['cherry','mango']
print(mylist)

# 3) insert()
# 리스트의 특정 인덱스에 데이터를 추가
print()
mylist = ['apple', 'banana']
mylist.insert(0,'cherry')
print(mylist)

# 4) clear()
# 리스트에 저장된 모든 요소를 삭제
print()
mylist = ['apple', 'banana']
mylist.clear()
print(mylist)

# 5) pop()
# 리스트의 마지막 요소가 반환되면서 삭제
print()
mylist = ['apple', 'banana']
item = mylist.pop()
print(item)
print(mylist)

# 6) remove()
# 인수로 전달된 값과 동일한 요소를 찾아서 제거, 동일한 요소가 여러 개인 경우에는 첫 번째 요소가 제거
print()
mylist = ['apple', 'banana','cherry','mango']
mylist.remove('cherry')
print(mylist) # ['apple', 'banana','mango']

mylist = ['apple', 'banana','cherry','mango', 'cherry']
mylist.remove('cherry')
print(mylist) # ['apple', 'banana','mango', 'cherry']


# 다음은 리스트에 포함된 잘못된 데이터를 모두 제거하는 프로그램
# 리스트에 저장된 정상 데이터는 모두 'a'를 포함한 문자열이며, 그렇지 않은 경우 잘못된 데이터입니다.

alist = ['above', 'cookie', 'app', 'about', 'bisket', 'apple', 'april']
 for i, item in enumerate(alist):
     if item.find('a') == -1:  # 또는 if 'a' not in item:
         print(f'{alist.pop(i)}이 제거됩니다.')

print(alist)
print(item.find('a'))