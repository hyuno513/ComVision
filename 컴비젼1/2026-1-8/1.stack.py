'''

추상 데이터 타입 abstract data type ADT
유사한 동작을 가진 자료구조의 클래스에 대한 수학적 모델
많은 추상 데이터 타입은 각기 클래스는 다르지만, 기능적으로는 동일하게 구현된 자료구조를 가질 수 있음
자료구조는 크게 배열 기반의 연속 방식과 포인터 기반의 연결 link  방식으로 분류,

스택 stack
배열의 끝에서만 데이터를 접근할 수 있는 선형 자료구조
스택은 배열 인덱스 접근이 제한되며, 후입선출 last in, first out LIFO 구조

스택의 추상자료형 ADT
데이터: 후입선출(LIFO)

'''

from typing import Any
# 리스트의 append()와 pop() 메서드로 스택을 구현
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool: # 스택이 비어있는지 확인
        return not bool(self.items)


    def push(self, value:int) -> None: # 스택 맨 끝(맨 위)에 항목을 삽입
        self.items.append(value) # 뒤에 쌓임

    def pop(self) -> Any: # 스택 맨 끝 항목을 반환하는 동시에 제거
        value = self.items.pop()
        # 만약에 value가 없는 경우 ??
        if value is not None:
            return value
        else:
            print('스택이 비어 있습니다')

    def size(self) -> int: # 스택의 크기를 확인
        return len(self.items) # len 함수: 길이를 재는 함수

    def peek(self) -> Any: # 스택 맽 끝 항목을 조회
        if self.items: # 어떤 값이 대입되는게 아님, 값이 있다면 실행됨
            return self.items[-1]
        else:
            print('Stack is empty')

    def __repr__(self) -> str: # 객체를 어떤 데이터 타입이던 객체를 문자열 표현으로 변환
        return repr(self.items)

# * 재사용할 수 있는 모듈 작성하기
# '__name__'은 모듈 이름을 나타내는 변수이고 작성 규칙은 다음과 같음
# 스크립트 프로그램이 직접 실행될 때 변수 __name__은 '__main__'.
# 스크립트 프로그램이 임포트될 때 변수 __name__ 은 원래 모듈 이름
# 다른 스크립트 프로그램에서 max_off()를 사용하려고 임포트하더라도 if 이하의 코드는 실행되지 않음

if __name__ == '__main__':
    stack = Stack()
    print(f'스택이 비어 있나요?{stack.isEmpty()}')
    for i in range(10):
        stack.push(i)
    print(f'스택크기:{stack.size()}')
    print(f'peek:{stack.peek()}')
    print(f'pop:{stack.pop()}')
    print(f'peek:{stack.peek()}')
    print(f'스택이비어있나요{stack.isEmpty()}')
    print(stack.isEmpty)
