"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""

# сначала решение в цикле для проверки рекурсивного решения
num = int(input('Количество элементов '))
elem = 1
sum_el = 1
for i in range(num):
    print(f'шаг: {i + 1}, элемент: {elem} сумма: {sum_el}')
    elem *= -0.5
    sum_el += elem


# теперь рекурсивное решение, кажется работает, но для меня понимается сложнее
def sum_elem(n):
    if n == 1:
        return 1
    return 1 + sum_elem(n - 1) * -0.5


for i in range(num):
    print(sum_elem(i + 1))
