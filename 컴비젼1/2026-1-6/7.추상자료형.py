# 추상 자료형 Abstract Data Type
# 프로그래머가 추상적으로 정의한 자료형
# 어떤 '자료들'과 자료에 가해지는 '연산들'을 구체적으로 표시
# 이 때 '추상'의 의미는 '어떤(what?)자료나 연산이 '제공'되는가만 정의하고
# 이들이 '어떻게(how?) 구현되는가'는 정의하지 않음

# 물건을 넣을 수 있는 가방(Bag)이라는 자료 구조에 대한 추상적인 자료형을 정의
# * 데이터: 지갑, 휴대폰, 거울, 동전 등 여러가지 물건을 넣을 수 있는 저장소. 여러개 저장도 가능
# * 연산: 가방으로 할 수 있는 일. 휴대폰을 넣거나 뺄 수 있어야 하고, 지갑이 가방에 있는지 확인할 수 있어야함
# 이를 연산으로 추가하면, 넣고 빼는 연산은 insert(), remove()라 하고,
# 물건이 있는지 확인하는 것은 contain()
# 물건의 개수 검사는 count()로 정의함

class Bag:
    def __init__(self):
        self.items = []

    def insert(self, item:str) -> None:
        self.items.append(item)

    def remove(self, item:str) -> None:
        if self. contain(item):
            self.items.remove(item)
        else:
            print(f'{item}은 가방에 없습니다.')

    def contain(self, item:str) -> bool:
        return item in self.items

    def count(self) -> int:
        return len(self.items) # 길이를 계산하는 함수

    def __str__(self) -> str:
        return str(self.items)

myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('손수건')
myBag.insert('지갑')
myBag.insert('빗')

print(f'가방에 {myBag.count()}개의 물건이 있습니다.')
print(myBag)

myBag.insert('손수건')
myBag.remove('빗')
print(myBag.contain('빗'))
print(myBag)