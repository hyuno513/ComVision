# CPU, RAM, VGA, SSD를 구성요소로 가지고 있는 Computer 클래스를 삽입해서 인스턴스를 생성하는 프로그램
# Computer 클래스는 각 구성요소의 값을 저장할 수 있는 set_spec() 메서드와 구성요소와 같음
# 출력할 수 있는 hardware_info() 메소드로 구성


class Computer():
    def set_spec(self, CPU, RAM, VGA, SSD):
        self.CPU = CPU
        self.RAM = RAM
        self.VGA = VGA
        self.SSD = SSD
    def hardware_info(self):
        print(f'CPU={self.CPU}')
        print(f'RAM={self.RAM}')
        print(f'VGA={self.VGA}')
        print(f'SSD={self.SSD}')

desktop = Computer()
desktop.set_spec('17', '16GB', 'GTX1060', '512GB')
print('desktop 스펙입니다')
desktop.hardware_info()

notebook = Computer()
notebook.set_spec('15', '8GB', 'MX300', '256GB')
print()
print('notebook 스펙입니다')
notebook.hardware_info()