
import threading
import time
import random

class Bank:
    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(1, 5):
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            p = random.randint(50,501)
            self.balance += p
            print(f'Пополнение: {p}. Баланс: {self.balance}\n')
            time.sleep(0.001)
    def take(self):
        for i in range(1, 5):
            p = random.randint(50,501)
            print(f'Запрос на {p}')
            if p <= self.balance:
                self.balance -= p
                print(f'Снятие: {p}. Баланс: {self.balance}\n')
            else:
                print('Запрос отклонен, недостаточно средств.\n')
                self.lock.acquire()


bk =  Bank()

t_1 = threading.Thread(target=Bank.deposit, args=(bk,))

t_2 = threading.Thread(target=Bank.take, args=(bk,))

t_1.start()
t_2.start()
t_1.join()
t_2.join()

print(f'Итоговый баланс: {bk.balance}')

