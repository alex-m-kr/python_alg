"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        res = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return res

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        sum_elem = 0
        for i in self.elems:
            sum_elem += len(i)
        return sum_elem

    def stack_count(self):
        return len(self.elems)


stack_plates = StackClass(4)
stack_plates.push_in('Первая')
stack_plates.push_in('Вторая')
stack_plates.push_in('Третья')
stack_plates.push_in('Четвертая')
stack_plates.push_in('Пятая')
stack_plates.push_in('Шестая')
print(stack_plates)
print(stack_plates.get_val())
print(stack_plates.pop_out())
print(stack_plates)
print(stack_plates.get_val())
print(stack_plates.stack_count())
print(stack_plates.stack_size())
