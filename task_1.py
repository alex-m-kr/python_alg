"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import memory_profiler
import string
import json
import math


# декоратор с memory_usage()
def my_decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


'''Первый скрипт, 1-й вариант
словарь с числами и буквами'''
@my_decor
@memory_profiler.profile
def func_1_1(line):
    dic1 = {numb: el for numb, el in enumerate(line, start=1)}
    return dic1


res, mem_diff = func_1_1(string.ascii_lowercase*1000)
print(f"Выполнение 1.1 заняло {mem_diff} Mib")


'''Первый скрипт, 2-й вариант
словарь с числами и буквами, используем сериализацию'''
@my_decor
@memory_profiler.profile
def func_1_2(line):
    dic1 = {numb: el for numb, el in enumerate(line, start=1)}
    json_str = json.dumps(dic1)
    del dic1
    return json_str


res, mem_diff = func_1_2(string.ascii_lowercase*1000)
print(f"Выполнение 1.2 заняло {mem_diff} Mib")

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     38.6 MiB     38.6 MiB           1   @my_decor
    43                                         @memory_profiler.profile
    44                                         def func_1_1(line):
    45     40.8 MiB      2.1 MiB       26003       dic1 = {numb: el for numb, el in enumerate(line, start=1)}
    46     40.8 MiB      0.0 MiB           1       return dic1


Выполнение 1.1 заняло 2.31640625 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    55     40.8 MiB     40.8 MiB           1   @my_decor
    56                                         @memory_profiler.profile
    57                                         def func_1_2(line):
    58     43.0 MiB      2.2 MiB       26003       dic1 = {numb: el for numb, el in enumerate(line, start=1)}
    59     44.9 MiB      1.9 MiB           1       json_str = json.dumps(dic1)
    60     42.9 MiB     -2.0 MiB           1       del dic1
    61     42.9 MiB      0.0 MiB           1       return json_str


Выполнение 1.2 заняло 1.8359375 Mib

На этом примере видно, что сериализация словаря json-формат и последующее удаление 
ссылки на словарь позволило получить выигрыш в памяти..
'''


'''Второй скрипт, 1-й вариант
список'''
@my_decor
@memory_profiler.profile
def func_2_1(line):
    list1 = [el for el in line]
    # print(list1)
    return list1


res, mem_diff = func_2_1(string.ascii_lowercase*10000)
print(f"Выполнение 2.1 заняло {mem_diff} Mib")


'''Второй скрипт, 2-й вариант
превращаем список в кортеж'''
@my_decor
@memory_profiler.profile
def func_2_2(line):
    list1 = [el for el in line]
    tuple1 = tuple(list1)
    del list1
    # print(tuple1)
    return tuple1


res, mem_diff = func_2_2(string.ascii_lowercase*10000)
print(f"Выполнение 2.2 заняло {mem_diff} Mib")

'''
Выполнение 2.1 заняло 2.83203125 Mib
Выполнение 2.2 заняло 2.0625 Mib
Кортеж менее затратный по памяти контейнер, т.к. не изменяемый.
'''


'''Третий скрипт, 1-й вариант
'''
@my_decor
@memory_profiler.profile
def func_3_1(lst):
    res = []
    for el in lst:
        res.append(math.factorial(el))
    return res


res, mem_diff = func_3_1(list(range(10000)))
print(f"Выполнение 3.1 заняло {mem_diff} Mib")


'''Третий скрипт, 2-й вариант
'''
@my_decor
@memory_profiler.profile
def func_3_2(lst):
    for el in lst:
        yield math.factorial(el)


my_gen, mem_diff = func_3_2(list(range(10000)))
print(f"Выполнение 3.2 заняло {mem_diff} Mib")


'''
Выполнение 3.1 заняло 73.43359375 Mib
Выполнение 3.2 заняло 0.0 Mib

при использовании генератора значения не хранятся в
памяти, а формируются в процессе обращения к ним, по мере запроса.
'''
