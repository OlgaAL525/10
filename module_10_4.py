import threading
import time
from queue import Queue
import random


class Table:
    def __init__(self, namber, guest=None):
        self.namber = namber
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 11))


class Cafe:
    def __init__(self, queue, *tables):
        self.queue = queue
        self.tables = tables
        self.k = 0

    def guest_arrival(self, *guests):
        i = 0
        for j in guests:
            if i < len(self.tables) and self.tables[i].guest == None:
                self.tables[i].guest = j.name
                j.start()
                print(f'{j.name} сел за стол номер {self.tables[i].namber}')
                i += 1
                self.k += 1

            else:
                self.queue.put(j)
                print(f'{j.name} в очереди')



    def discuss_guests(self):
        while self.queue.empty() == False or self.k != 0 :
            for i in self.tables:
                if i.guest != None and Guest(i.guest).is_alive() == False:
                    print(f'{i.guest}  поел и ушел')
                    print(f'Стол {i.namber} свободен')
                    i.guest = None
                    self.k -= 1

                elif i.guest == None and self.queue.empty() == False:
                    b = self.queue.get()
                    i.guest = b.name
                    print(f'{b.name} вышел из очереди и сел за стол номер {i.namber}')
                    b.start()
                    self.k += 1



tables = [Table(namber) for namber in range(1, 5)]
guests_names = ['Олег', 'Иван', 'Никита', 'Павел', 'Илья', 'Андрей']
guests = [Guest(name) for name in guests_names]
queue = Queue()
cafe = Cafe(queue, *tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()