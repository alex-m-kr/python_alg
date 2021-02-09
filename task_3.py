"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from statistics import median
import random

m = int(input('m: '))
lst = [random.randint(1, 100) for _ in range(2 * m + 1)]
# lst= [3, 4, 3, 3, 5, 3, 3]
print('Список:')
print(lst)
print('Результат через median:', median(lst))
# print(sorted(lst))
print('==============')


def func_median(lst_obj):
    """За медиану принимается поочередно каждый элемент копии списка и
    удаляется. Затем пока список не закончится, наполняются левый и правый
    списки минимальными и максимальными оставшимися элементами, которые также
    после этого последовательно удаляются. Если правый элемент левого списка
    не больше медианы, а левый элемент правого списка не меньше, то всё.
    Иначе проверяем на медиану следующей элемент и т.д.
    """
    cp_lst_obj = lst_obj[:]
    left = []
    right = []
    # cnt = 0
    for i in range(len(cp_lst_obj)):
        med = cp_lst_obj.pop(i)
        # print(med)
        # print(cp_lst_obj)
        while cp_lst_obj:
            # cnt += 1
            max_el = max(cp_lst_obj)
            min_el = min(cp_lst_obj)
            # print(max_el, min_el)
            right.insert(0, max_el)
            left.append(min_el)
            cp_lst_obj.remove(max_el)
            cp_lst_obj.remove(min_el)
        if left[-1] <= med <= right[0]:
            print(left, right)  #  для проверки работы
            # print(cnt)
            return med
        left.clear()
        right.clear()
        cp_lst_obj = lst_obj[:]


print('Результат работы написанной функции:', func_median(lst))
