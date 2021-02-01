"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""
# 1-й вариант
from collections import defaultdict
'''Не совсем понял, зачем нужно представлять числа в виде "массивов",
может быть надо прописать какую-то свою логику работы с 16-ми числами,
в этом решении. Вывод в виде [‘A’, ‘2’] только для соответствия задаче,
работа идет со входными стринговыми данными.
Но внешне выглядит, как в условии задачи.
'''


first_num = input('Первое шестнадцатеричное число: ')
second_num = input('Второе шестнадцатеричное число: ')
first_d = defaultdict(list)
second_d = defaultdict(list)
for dig in first_num:
    first_d['num'].append(dig)
for dig in second_num:
    second_d['num'].append(dig)
print('Введенные числа по условиям задачи выводятся как', first_d['num'], second_d['num'])
# print(first_d)
# print(second_d)
res_sum = hex(int(first_num, 16) + int(second_num, 16))
res_mult = hex(int(first_num, 16) * int(second_num, 16))
# print(res_sum, res_mult)

sum_d = defaultdict(list)
mult_d = defaultdict(list)
for dig in res_sum[2:]:
    sum_d['num'].append(dig.upper())
for dig in res_mult[2:]:
    mult_d['num'].append(dig.upper())
print(f"сумма чисел: {sum_d['num']}, произведение чисел: {mult_d['num']}")

print('-----------------------------------------------------------------------')
# второй вариант через ООП


class HexNumber:
    def __init__(self, h_str):
        self.h_str = h_str

    def output(self):
        print(list(self.h_str), end=' ')

    def __add__(self, other):
        print('Складываем числа')
        self.output()
        other.output()
        res_summ = hex(int(self.h_str, 16) + int(other.h_str, 16))
        res_summ = [i.upper() for i in res_summ[2:]]
        print('Сумма чисел равна:', res_summ)

    def __mul__(self, other):
        print('Умножаем числа')
        self.output()
        other.output()
        res_mul = hex(int(self.h_str, 16) * int(other.h_str, 16))
        res_mul = [i.upper() for i in res_mul[2:]]
        print('Произведение чисел равно:', res_mul)


hx1 = HexNumber(first_num)
hx2 = HexNumber(second_num)

hx1 + hx2
hx1 * hx2
