# 개인정보의 보안 처리를 위하여 주어진 인수의 일부를 *로
# 바구어 변환하는 함수를 만들어서 이를 모듈로 저장하는 프로그램

# 모듈명 : mysecure.py
# secure_name()함수 : 김철수 -> 김**
# secure_no() 함수: 951012-1234567 -> 951012-1******
# secure_phone() 함수 : 010-1234-5678 -> 010-****-5678

# mysecure.py를 불러오기

from mysecure import *


print(secure_name('김철수'))

print(secure_no('951012-1234567'))

print(secure_phone('010-1234-5678'))