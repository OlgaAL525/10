import time
import threading
import io

def write_words(word_count, file_name):
    k = file_name
    with open(k, 'a', encoding = 'utf-8') as file:
        for i in range(1, (word_count+1)):
            file.write(f'Слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {k}')


t_0 = time.time()
write_words(10, 'e_1.txt')
write_words(30, 'e_2.txt')
write_words(200, 'e_3.txt')
write_words(100, 'e_4.txt')
t_1 = time.time()
print(f'Работа потоков {round((t_1-t_0), 2)}c')

t_2 = time.time()
tr_5 = threading.Thread(target=write_words, args=(10,'e_5.txt'))
tr_6 = threading.Thread(target=write_words, args=(30,'e_6.txt'))
tr_7 = threading.Thread(target=write_words, args=(200,'e_7.txt'))
tr_8 = threading.Thread(target=write_words, args=(100,'e_8.txt'))
tr_5.start()
tr_6.start()
tr_7.start()
tr_8.start()
tr_5.join()
tr_6.join()
tr_7.join()
tr_8.join()
t_3 = time.time()
print(f'Работа потоков {round((t_3-t_2), 2)}c')
