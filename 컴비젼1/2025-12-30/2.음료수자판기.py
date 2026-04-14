# 700원 음료수를 뽑을 수 있는 자판기 프로그램
# 돈을 넣으면 몇 잔의 음료수를 봅을 수 있는지 그리고 잔돈은 어마인지 모든 경우를 출력

# def vending_machine(money)

# 실행 예)
# 음료수 = 0개, 잔돈 = 3000원
# 음료수 = 1개, 잔돈 = 2300원
# 음료수 = 2개, 잔돈 = 1600원
# 음료수 = 3개, 잔돈 = 900원
# 음료수 = 4개, 잔돈 = 200원

def vending_machine(money):
    price = 700
    count = money // price +1
    for drink in range(count):
        change = money - drink * price
        print(f'음료수 = {drink}개, 잔돈= {change}')


vending_machine(5000)
