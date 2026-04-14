# 클래스와 객체
# 1. 객체의 개념
# 개발을 하다보면 정수나 실수 또는 문자열 등 기본적인 자료형으로 표현하기 힘든것들이 존재
# 예를 들어 어떤 게시글을 파이선으로 표현을 한다면
# 게시글 번호, 제목, 작성자, 비밀번호, 내용, 최초작성일자, 최종수정일자, 조회수가 필요한데
# 이를 손쉽게 관리 하려면 8개의 항목을 하나의 이름을 가진 객체 object로 만들어서 사용하는 것이 좋다

# 클래스의 개념
# 클래스는 객체를 만드는 도구
# 하나의 클래스를 만들어두면 그 클래스를 통해서 동일한 구조를 가진 여러개의 객체를 만들 수 있음
# 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질수 있음
# 인스턴스 instance 역시 클래스를 이용해서 생성한 객체를 가르키는 용어

# 객체와 인스턴스의 미묘한 차이
# 1) 와플머신 클래스로 만든 와플은 객체 object
# 2) 와플은 와플머신 클래스의 인스턴스 isntance

# 비유
# 클래스: 붕어빵을 찍어내는 틀
# 객체: 틀에서 찍어나온 붕어빵 그 자체
# 인스턴스: 특정 붕어빵과 틀의 관계에 집중한 표현

# 3. 클래스 정의
# 클래스 정의 방법
# 1) class 키워드로 클래스를 정의
# 2) 클래스 일므은 Upper Camel Case 규칙을 따름
# 파이썬은 변수나 함수의 이름을 네이밍할때 언더바 _ 를 이용해 단어를 연결하는 Snake Case 방식을 사용하지만
# 클래스는 Upper Camel Case 규칙을 따름
# print + member : printmember 1)print_member 2) printMemeber 3) PrintMember


# 클래스(설계도) 정의
class Dog:
    def __init__(self, name):
        self.name = name

# 2. 객체 생성
my_dog = Dog("초코") # 객체, my_dog는 Dog의 인스턴스다
print(my_dog.name)
print(my_dog) # <__main__.Dog object at 0x000001C3CA8870E0>: 주소값
your_dog = Dog("인절미") # 객체, your_dog는 Dog의 인스턴스다
print(your_dog.name)
print(your_dog)

# 원시타입: 변수 자체에 값이 담긴다.
# 참조타입: 메모리의 주소값이 담긴다.

# 객체를 생성하시오 -> 메모리에 올릴 실체를 만드시오
# 인스턴스 타입 확인 -> 이 객체가 어떤 클래스로부터 만들어진것인지 타입을 체크

print(isinstance(my_dog, Dog)) # my_dog는 Dog클래스에서 나온 인스턴스가 맞습니까?

# 클래스의 구성
# 1. 클래스의 기본 구성
# 객체를 만들어내는 클래스는 객체가 가져야 할 값과 기능을 가지고 있어야함
# 값은 변수, 기능은 함수
# 클래스는 변수와 함수로 구성됨

# 클래스를 구성하는 변수는 1) 클래스를 기반을 ㅗ생성된 모든 인스턴스들이 공유하는 변수인 클래스 변수와
# 2) 모든 인스턴스들이 개별적으로 가지는 변수인 인스턴스 변수로 분리

# 클래스를 구성하는 함수는 메소드 method라 하고
# 1) 클래스 메소드 2) 정적 메소드 3) 인스턴스 메소드로 분리

# 2. 인스턴스 변수와 인스턴스 메소드
# 인스턴스 변수란 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수
# 모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줌
# 인스턴스 메소드란 인스턴스 변수를 사용하는 메소드
# 인스턴스 메소드는 반드시 첫번째 매개변수로 self로 추가해야함

class Person:
    # 첫번째 매개변수가 self이므로 self란 인스턴스 메소드
    # 모든 인스턴스는 who_am_i() 메소드를 호출할 수 있음.
    def who_am_i(self, name, age, tel, address):
        self.name = name # 인스턴스 주소값에 name이라는 공간을 할당받아 그 주소값에 name의 내용이 들어간다.
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()
print(boy)
# print(boy.name) # error

boy.who_am_i('maresca',20,'1234-5678', 'daegu')
print(boy.name)


# __init__ = 생성자

class Student:
    def __init__(self, name, department, professor, phone, address, grade):
        self.name = name
        self.department = department
        self.professor = professor
        self.phone = phone
        self.address = address
        self.grade = grade

student1=Student('enzo', '123', 'kroos', '1234-5678', 'london', '123')

print(student1.name)