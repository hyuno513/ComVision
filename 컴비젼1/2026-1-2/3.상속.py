# 상속
# 1. 상속이란?
# 어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 만들 수 있음
# 다른 클래스의 기능을 물려받을 대 상속받는다는 표현을 사용
# 그래서 상속 관계에 있는 클래스를 표현할 대 부모 클래스와 자식 클래스하는 말을 사용

# 부모 클래스 : 상속해 주는 클래스 / 슈퍼 클래스 super class, 기반 클래스 base class
# 자식 클래스: 상속 받는 클래스/ 서브 클래스 sub class, 파생 클래스 derived class

# 2. 상속 관계 규현
# 기본적으로 두 클래스가 상속 관계에 높이려면 IS-A 관계가 성립해야 함
# IS-A 관계란 '~은 ~이다. 로 해설할 수 있는 관계를 의미
# 희생은 사람이다 Student is a Person 처럼 해석되는 것이 IS-A 관계
# 이미 Student 는 서브 클래스가 되고, Person은 슈퍼 클래스가 됨

# 컴퓨터 과학에서 상속은 is-a 관계를 갖고 있을 대 사용
# is-a 관계는 '직원은 사람이다 employee is-a person' 또는 '자동차는 차량이다 car is-a vehicle'이라고 부른다
# has-a 관계는 컴퓨터 과학 용어도 '그릇이 스쿱을 갖는다 Bowl has-a Scoop'라고 부르고,
# has-a 관계는 상속이 아니라 구성 Composition으로 구현함.

# 객체 지향 프로그래밍을 처음 접하면 두 클래스가 어떤 관계를 갖고 있을 때, 반드시 상속 관계가 만들어져야한다고
# 생각하는 경우가 많음
# is-a 관계를 가질 경우에는 상속, has-a 관계를 가질 경우에는 구성을 사용한다고 구분해서 생각하면
# 어떤 경우에 상속등을 활용해야 하는지 조금 더 쉽게 구분


# 상속의 기본적인 형식
# class 슈퍼 클래스:
# 본문

# class 서브 클래스(슈퍼클래스):
# 본문

# 서브클래스를 구현할 대는 괄호 안에 어떤 슈퍼 클래스를 상속받는지 명시
# 상속 관계에 놓인 서브 클래스는 마치 자신의 것처럼 슈퍼 클래스의 기능을 사용할 수 있음

class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + "가 " + food +'을 먹습니다.')

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(self.name+'는 '+self.school+'에서 공부를 합니다.')

potter = Student('포터', '스탬포드')
potter.eat('경질')
potter.study()


# 서브 클래스의 __init__()
# 서브 클래스의 생성자를 구현할 대는 반드시 슈퍼 클래스의 생성자를 먼저 호출하는 코드를 작성해야 함
# super라는 키워드는 슈퍼 클래스를 의미

class Computer:
    def __init__(self):
        print('슈퍼 클래스의 생성자가 실행되었습니다.')

class NoteBook(Computer):
    def __init__(self):
        super().__init__()
        print('서브 클래스의 생성자가 실행되었습니다.')

n = NoteBook()

# 4. 서브 클래스와 인스턴스 자료항
# 슈퍼 클래스 객체는 슈퍼 클래스의 인스턴스
# 그에 비해 서브 클래스 객체는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
# 즉 서브 클래스 Student의 객체는 서브 클래스 Student의 인스턴스 이면서
# 동시에 슈퍼 클래스 Person의 인스턴스

# 어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서 isinstance()함수를 사용
# 객체가 인스턴스일 경우에는 True 아니면 False 반환
# instance(객체, 클래스)
print(isinstance(potter, Student))
print(isinstance(potter, Person))

