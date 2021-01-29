"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

'''
сперва попробовал сделать так: использовать функцию map, создать список
из кортежей (количество вхождений, число), отсортировать его и выдать 
из последнего, где макс. кол-во вхождений элементы.
Но, вижу, что по времени это не самый оптимальный алгоритм, 
хотя по количеству строк - самый короткий
'''
def func_3():
    max_array = map(lambda x: (array.count(x), x), array)
    res = sorted(list(max_array))[-1]
    return f'число {res[1]} встречается раз {res[0]}'


print(func_1())
print(func_2())
print(func_3())


# timeit
print('первый вариант',
    timeit('func_1()', setup='from __main__ import func_1',
    number=1000000))

print('второй вариант',
    timeit('func_2()', setup='from __main__ import func_2',
    number=1000000))

print('третий вариант',
    timeit('func_3()', setup='from __main__ import func_3',
    number=1000000))
