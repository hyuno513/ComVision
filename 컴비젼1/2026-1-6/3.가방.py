# 가방을 만들때마다 현재 만들어진 가방이 몇개인지 계산할 수 있는 Bag 클래스
class Bag:
    count = 0

    def __init__(self):
        Bag.count += 1

    @classmethod
    def remain_bag(cls):
        return cls.count

    @classmethod
    def sell(cls):
        cls.count -= 1



print(f'현재 가방 {Bag.remain_bag()}')
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 {Bag.remain_bag()}')
bag1.sell()
bag2.sell()
print(f'현재 가방 {Bag.remain_bag()}')