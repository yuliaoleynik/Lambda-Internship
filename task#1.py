import time

def uniqueValues(file_dict):
    file_list = []

    for i in range(20):
        file_list += file_dict[i]

    print("Уникальных словосочетаний:", len({}.fromkeys(file_list).keys()))      
  

def existInAllFiles(file_dict):
    exist = set(file_dict[0])

    for i in range(1, 20):
        file = set(file_dict[i])
        exist = {x for x in exist if x in file}

    print("Словосочетаний, которые есть во всех 20 файлах:", len(exist))


def existInAtLeastTen(file_dict):
    file_list = []
    exist = {}

    for i in range(20):
        for word in set(file_dict[i]):

            if word in exist.keys():
                exist[word] += 1
            else:
                exist[word] = 1

    file_list = [text for text, count in exist.items() if count > 9]

    print("Словосочетаний, которые есть, как минимум, в десяти файлах:", len(file_list))


start_time = time.time()
file_dict = {}

for i in range(20):
    with open(f'out{i}.txt', 'r') as file:
        file_dict[i] = file.read().splitlines()

uniqueValues(file_dict)
existInAllFiles(file_dict)
existInAtLeastTen(file_dict)

print("Время выполнения:", time.time() - start_time, "seconds")     

