"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskB:
    def __init__(self):
        self.base_q = QueueClass()
        self.rev_q = QueueClass()

    def resolve(self):
        task = self.base_q.from_queue()

    def revison(self):
        task = self.base_q.from_queue()
        self.rev_q.to_queue(task)

    def to_base_q(self, item):
        self.base_q.to_queue(item)

    def from_rev(self):
        task = self.rev_q.from_queue()
        self.base_q.to_queue(task)

    def base_task(self):
        return self.base_q.elems[len(self.base_q.elems) - 1]

    def rev_task(self):
        return self.rev_q.elems[len(self.rev_q.elems) - 1]

qc_obj = TaskB()
qc_obj.to_base_q('первая задача')
qc_obj.to_base_q('вторая задача')
qc_obj.to_base_q('третья задача')
print(qc_obj.base_task())
qc_obj.resolve()
print(qc_obj.base_task())
qc_obj.revison()
print(qc_obj.rev_task())
print(qc_obj.base_task())
