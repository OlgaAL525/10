import threading
import time
from queue import Queue
import random

class Table:
    def __init__(self, namber, guest = None):
        self.namber = namber
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        time.sleep(random.randint(3,11))

class Cafe:
    def __init__(self, queue, *tables):
        self.queue = queue
        self.tables = tables
    def guest_arrival(self, *guests):
        i = 0

        for j in guests:
            while i < len(self.tables):
                if self.tables[i].guest == None:
                    self.tables[i].guest = j
                    j.start()
                    print(f'{j.name} сел за стол номер {self.tables[i].namber}')
                    i += 1
                    break

            queue.put(j)
            print(f'{j.name} в очереди')



    # def discuss_guests(self):
    #     if not self.queue.empty():
    #         for i in self.tables:
    #             if i.guest != None and not self.guest.is_alive():
    #                 print(f'{guest.name} за {i} поел и ушел')
    #                 print(f'Стол {i} свободен')
    #             elif i.guest != None:
    #                 b = self.queue.get()
    #                 i.guest = b.name
    #                 print(f'{b.name} вышел из очереди и сел за стол номер {i}')
    #                 b.start()


tables = [Table(namber) for namber in range(1,3)]
guests_names = ['Олег','Иван','Никита','Павел','Илья','Сергей','Андрей','Игорь']
guests = [Guest(name) for name in guests_names]
queue = Queue()
cafe = Cafe(queue,*tables)
cafe.guest_arrival(*guests)
# cafe.discuss_guests()


