import time
from multiprocessing import Pool

def read_info(name):
    all_data = list()
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)
    return all_data


filenames = [f'file{n}.txt' for n in range(1,3)]

# t1 = time.time()
# for i in filenames:
#     read_info(i)
# t2 = time.time()
#
# print((t2-t1))


if __name__ == '__main__':
    t1 = time.time()
    with Pool(2) as p:
        p.map(read_info, filenames)
    t2 = time.time()
    print((t2 - t1))

