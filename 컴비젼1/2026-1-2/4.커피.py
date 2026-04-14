# 원두(bean)을 지정하는 Coffee 클래스와 원두(bean)에 물을 섞은 Espresso 클래스를 상속
class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print(f'원두 : {self.bean}')

class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print(f'물: {self.bean}ml')

class Americano(Espresso):
    def __init__(self, bean, water, more_water):
        super().__init__(bean, water)
        self.more_water = more_water

    def americano_info(self):
        super().espresso_info()
        print(f'물 더: {self.more_water}ml')

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

coffee2 = Americano('파나마', 20, 200)
coffee2.americano_info()