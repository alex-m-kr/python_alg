"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict
import string

simple_dic = {el: el for el in string.ascii_lowercase[::-1]}
# print(simple_dic)
# print(len(simple_dic))
order_dic = OrderedDict({el: el for el in string.ascii_lowercase[::-1]})
# print(order_dic)
# print(len(order_dic))

def fun_simple_dic(dic):
    for i in range(len(dic)):
        res = dic.popitem()
        # print(res, end='')
    # print('\n', dic)

def fun_ord_dic(dic):
    for i in range(len(dic)):
        res = dic.popitem()
        # print(res, end='')
    # print('\n', dic)


def fun_simple_dic2(dic):
    for i in string.ascii_lowercase:
        res = dic.get(i)
    #     print(res, end='')
    # print()

def fun_ord_dic2(dic):
    for i in string.ascii_lowercase:
        res = dic.get(i)
        # print(res, end='')

# fun_simple_dic2(simple_dic)
# fun_ord_dic2(order_dic)


print(timeit("fun_simple_dic(simple_dic)", globals=globals()))
print(timeit("fun_ord_dic(order_dic)", globals=globals()))
print('Вторые замеры --------------------------------------- ')
print(timeit("fun_simple_dic2(simple_dic)", globals=globals()))
print(timeit("fun_ord_dic2(order_dic)", globals=globals()))

'''
1) обычный словарь, 2) упорядоченный словарь
Первый замер производился на popitem() (returns and removes a (key, value) pair)
Второй замер на get.

0.5599751380004818
0.5383312800004205
Вторые замеры --------------------------------------- 
3.5336638500002664
3.5956654330002493

По времени на этих двух примерах разница не существенная.
Делаю вывод, что в Python старше 3.6 OrderedDict есть смысл использовать, 
только если нужен дополнительный функционал, например, 
move_to_end (перемещает существующий ключ в любой конец упорядоченного словаря).
У обычных словарей такого метода нет.
'''
