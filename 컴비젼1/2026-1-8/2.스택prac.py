# 문자열 반전하기
# 스택은 데이터를 역순으로 정렬하거나 검색할 때 사용가능
# 3.스택의 스택 클래스를 사용하여 문자열을 뒤집어 볼것

from stack_simple_01 import Stack


def reserve_string_with_stack(str1 : str) -> str:
    stack = Stack()
    revStr = ''
    # str1을 stack에 한글자씩 넣어줘야한다.
    for i in str1:
        stack.push(i)

    # 무한루프 -> 만약 스택이 비어있지 않다면
    # revStr -> 한글자씩 집어넣기
    while not stack.isEmpty():
        revStr += stack.pop()

    return revStr


if __name__ == '__main__':
    str1 = '소독용 에탄올 스왑!'
    print(str1)
    print(reserve_string_with_stack(str1))