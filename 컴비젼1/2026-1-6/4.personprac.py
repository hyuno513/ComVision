# 오류

class Person:
    count = 0


# 객체를 만들때 제일 처음 실행되는 초기화 메서드이다. 전달받는 인자가 self 외에 다른 것이 있다면 객체를 생성할때 인잣값으로
# 넘겨주면 __init__ 메스드에서 사용한다.
def __init__(self, name):
    self.name = name
    Person.count += 1


# 객체 자체를 출력할 때 념겨주는 형식을 지정해주는 메서드이다.
def __str__(self) -> str:
    return f'{self.name} is born'

# 인스턴스가 생성될때 생기는 __init__ 처럼 삭제될때 일어나는 메서드이다.
def __del__(self):
    print(f'{self.name} is dead')
    Person.count -= 1

@classmethod
def get_population(cls):
    return Person.count

man = Person('james')
print(man)
woman = Person('emily')
print(woman)
print(f'전체인구수:{Person.get_population()}명')
del man # 강제 소멸 함수
print(f'전체 인구수 : {Person.get_population()}명')