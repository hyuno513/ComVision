# miles, pound는 단위 변환에서 사용하는 변수

MILES = 0.621371 # 1km
POUND = 0.002205 # 1gm

def kilometer_to_miles(kilometer):
    return kilometer * MILES

def gram_to_pounds(gram):
    return gram * POUND
