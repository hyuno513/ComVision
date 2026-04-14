# 1. 모듈이란
# 모듈 module이란 한 마디로 파이썬 파일(.py)
# 언제든지 사용할 수 있도록 변수나 함수 도는 클래스를 모아 놓은 파일

# 2. 모듈생성
# converter.py 생성

# 3. 모듈의 사용
# 반드시 같은 디렉토리에 있어야함
# 모듈에 저장된 함수를 사용하는 방법
# 1. 모듈 전체를 가져오는 방법
# 모듈에 저장된 모든 클래스나 함수를 사용하고자 할 때
# 예) import 모듈

import converter

miles = converter.kilometer_to_miles(150)
print(f'150km={miles}miles')

pounds = converter.gram_to_pounds(1000)
print(f'1000={pounds}pounds')

# 2. 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법
# 예) from 모듈 import 함수
# 예) from 모듈 import 함수1, 함수2
# 예) from 모듈 import *

from converter import kilometer_to_miles # 모듈은 가져오지 않고 특정 함수만 가져옴

# 3. 별명사용하기
print(0)
import converter as cvt



