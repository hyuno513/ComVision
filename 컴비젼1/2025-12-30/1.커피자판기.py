# 커피 자판기 프로그램
# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 있는 커피의 종류와 가격
# 아메리카노: 1000, 카페라떼: 1500, 카푸치노: 2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환
# 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환
# 5. 정상 주문이면 주문한 커피와 잔돈을 반환

def coffee_machine(money, pick):
    print(f'{money}원이 {pick}를 선택했습니다.')
    menu = {
        '아메리카노' : 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }
    if pick not in menu: # 없는 커피 주문
        print(f'{pick}는 판매하지 않습니다.')
        return money, '없는메뉴'
    elif menu[pick] > money: # 구매할 금액이 부족한 경우
        print(f'{pick}는 {menu[pick]}원입니다.')
        return money, '금액부족'
    else: # 정상주문이면 잔돈과 선택한 커피를 반환
        return money - menu[pick], pick


order = input('커피를 선택하세요.>>')
pay = int(input('얼마를 낼래요>>'))

change, coffee = coffee_machine(pay, order)
print(f'잔돈{change}원, 커피 {coffee}')

