# 소멸자
# 인스턴스가 생성될 때 자동으로 호출되는 생성자와 마찬가지로
# 인스턴스가 소멸될 때 자동으로 호출되는 매서드
# 소멸자는 __del__()

class Sample:
    def __init__(self):
        print('생성자 실행')

    def __del__(self):
        print('소멸자 실행')

Sample = Sample()