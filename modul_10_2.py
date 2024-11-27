import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали татары!')
        i = 100
        j = 0
        while i:
            i -= self.power
            j +=1
            time.sleep(1)
            print(f'{self.name} сражается {j} минут, осталось {i} татар')
        print(f'{self.name} одержал победу!')

b_1 = Knight('Добрыня Никитич', 20)
b_2 = Knight('Алеша Попович', 10)

b_1.start()
b_2.start()

b_1.join()
b_2.join()

print('Все битвы закончились')
