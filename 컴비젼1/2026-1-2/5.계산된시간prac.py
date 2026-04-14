class Watch:
    def What(self):
        time = input('시간을 입력하세요 >>')
        time_list = time.split(':')
        self.hour = int(time_list[0])
        self.minute = int(time_list[1])
        self.second = int(time_list[2])

    def see(self):
        print(f'계산된 시간은{self.hour}시, {self.minute}분, {self.second}초입니다.')


watch = Watch()
watch.What() # -> 시간을 입력하세요
watch.see() # -> 계산된시간은