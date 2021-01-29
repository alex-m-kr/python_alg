"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


'''
буду разбираться с этой задачей
взял алогоритм из инета, немного изменил
до 168 работает, а потом нетn = 1000
numb = int(input('номер числа '))
cnt = 0
sieve = set(range(2, n+1))
while sieve:
    cnt +=1
    if cnt > numb:
        break
    prime = min(sieve)
    print(prime, end = "\t")
    sieve -= set(range(prime, n+1, prime))
print('\n', prime)

'''

n = 1000
numb = i
cnt = 0
sieve = set(range(2, n+1))
while sieve:
    cnt +=1
    if cnt > numb:
        break
    prime = min(sieve)
    # print(prime, end = "\t")
    sieve -= set(range(prime, n+1, prime))
print('\n', prime)
