"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


N = 10000  # размер списка, словаря


# заполнение списка
def my_lst_create():
    start_val = time.time()
    my_lst = [i for i in range(N)]
    end_val = time.time()
    return my_lst, end_val - start_val


res_lst, sekond_l = my_lst_create()

print(f'Время создания списка {sekond_l} сек')
# print(res_lst)


# заполнение словаря, словарь заполняется дольше за счет формирования хеш-таблицы
def my_dict_create():
    start_val = time.time()
    my_dict = {i: i for i in range(N)}
    end_val = time.time()
    return my_dict, end_val - start_val


res_dict, sekond_d = my_dict_create()

print(f'Время создания словаря {sekond_d} сек')
# print(res_dict)

# операции со списком
start_val = time.time()
for i in range(N):
    position = res_lst.index(i)
    # print(position)
end_val = time.time()
print(f'Время возврата индексов элементов списка {end_val - start_val} сек')

# операции со словарем, видно что сходные операции работают быстрее списка за счет хеш-таблиц, константная сложность
start_val = time.time()
for i in range(N):
    value = res_dict.get(i)
    # print(value)
end_val = time.time()
print(f'Время возврата значений по ключу {end_val - start_val} сек')
