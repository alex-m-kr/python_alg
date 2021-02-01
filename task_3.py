"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from timeit import timeit
from collections import deque
import string


simple_list = list(string.ascii_lowercase)
deq_obj = deque(simple_list)

simple_list2 = list(string.ascii_lowercase)
deq_obj2 = deque(simple_list)


def fun_list():
    for i in range(len(simple_list)):
        simple_list.insert(0, i)


def fun_deque():
    for i in range(len(deq_obj)):
        deq_obj.appendleft(i)


def fun_list2():
    for i in range(len(simple_list2)):
        simple_list2.append(i)


def fun_deque2():
    for i in range(len(deq_obj2)):
        deq_obj2.append(i)


# fun_list()
# fun_deque()
# fun_list2()
# fun_deque2()

# print(simple_list)
# print(deq_obj)
# print(simple_list2)
# print(deq_obj2)

print(timeit("fun_list()", globals=globals(), number=12))
print(timeit("fun_deque()", globals=globals(), number=12))
print('Вторые замеры --------------------------------------- ')
print(timeit("fun_list2()", globals=globals(), number=12))
print(timeit("fun_deque2()", globals=globals(), number=12))

# print(len(simple_list))
# print(len(deq_obj))
# print(len(simple_list2))
# print(len(deq_obj2))

'''Разница в скорости должна проявиться при добавлении в начало: 
appendleft против insert
В данном случае наши объекты (list и deque) с каждым разом увеличиваются, 
поэтому очень быстро (в данном примере через 12 запусков) становится
ощутимой разница в скорости при добавлении в начало.
deque гораздо быстрее.

Замеры: 1)list; 2) deque

4.498539686999948
0.017181910000090284

А вот при добавлении в конец, наоборот списки совсем немного выигрывают:

Вторые замеры --------------------------------------- 
0.01643043000012767
0.018208193000191386
'''
