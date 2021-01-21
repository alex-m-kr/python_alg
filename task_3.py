"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
string = 'рара'
substring_dic = {}
for i in range(len(string) - 1, 0 , -1):
    for j in range(len(string)):
        substring = string[j:j+i]
        substring_dic[hash(substring)] = substring
for key in substring_dic:
    print(substring_dic.get(key))
print('Количество подстрок', len(substring_dic.keys()))
# print(substring_dic)
