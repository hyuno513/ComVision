# 파이썬으로 영어사전을 구현하고자 한다.
# 다음과 같은 딕셔너리를 하나 생성하고 실행 예외 같이 동작하는 프로그램

english_dict = {
    'flower' : '꽃',
    'fly' : '날다',
    'floor' : '바닥'
}

a = input(str('영어 단어를 입력하세요 >>>'))
print(english_dict[a])