"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


numb = 123456789   # тестовое число
# print(revers_1(numb))
# print(revers_2(numb))
# print(revers_3(numb))


# cProfile
def main():
    number = 123456789
    res1 = revers_1(number)
    res2 = revers_2(number)
    res3 = revers_3(number)


run('main()')

# timeit
print('первый вариант',
    timeit('revers_1(numb)', setup='from __main__ import revers_1, numb',
    number=1000000))

print('второй вариант',
    timeit('revers_2(numb)', setup='from __main__ import revers_2, numb',
    number=1000000))

print('третий вариант',
    timeit('revers_3(numb)', setup='from __main__ import revers_3, numb',
    number=1000000))

'''
замеры времени
первый вариант 4.429710866999812
второй вариант 2.808727779000037
третий вариант 0.6035289679984999
Выводы:
1-я рекурсивная функция самая низкоэффективная, это видно по времени, а
также по количеству совершенных вызовов ncalls - 10.
3-й алгоритм самый эффективный, срез строки сработал быстрее всего,
здесь нет необходимости выполнять каждый раз арифметические операции 
деления (% //), количество которых равно количеству цифр в числе
'''
