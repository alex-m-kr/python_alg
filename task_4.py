"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex
my_cache_dic = {}  # словарь будте хранилищем кэша url


def func4(url, cache_dic=my_cache_dic):
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_hash in cache_dic:
        print(f'В кэше уже есть страница {url} с хешем {url_hash}')
    else:
        print(f'Добавляем страницу {url} с хешем {url_hash} в кэш')
        cache_dic[url_hash] = url


func4('ya.ru')
func4('r0.ru')
func4('ya.ru')
func4('r0.ru')
print(my_cache_dic)
