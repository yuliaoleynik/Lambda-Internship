def DotsComb(*chars, repeat=1):
    dots = [tuple(pool) for pool in chars] * repeat
    variants = [[]]

    for elem in dots:
        temp = []
        for i in variants:
            for j in elem:
                temp.append(i + [j])                                  # декартово произведение подсписка комбинаций и (".", "")

        variants = temp           
    
    for comb in variants:
        yield tuple(comb)


word = input("Please, enter the word :")
combinations = []                                                     # массив(список) комбинаций

for dots in DotsComb((".", ""), repeat=len(word) - 1):                # кортеж разных расположений точек и их кол-во
    new = [char for tpl in zip(word, dots + ("",)) for char in tpl]   # запись новой комбинации во временный список (перебор символов слова и точек из кортежей zip)
    combinations.append("".join(new))                                 # объединение списка в строку и добавление новой комбинации в основной список 

print(combinations)  
