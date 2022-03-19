class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': int(input('Введите оклад')), 'bonus': int(input('Введите премию'))}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._Worker__income['wage'] + self._Worker__income['bonus'])


worker_1 = Position('Алексей', 'Тмин', 'CEO')
worker_1.get_full_name()
worker_1.get_total_income()
