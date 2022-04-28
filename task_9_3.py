class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.position}: {self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


person_1 = Position('Ivan', 'Ivanov', 'manager', 10000, 5000)
print(person_1.name)
print(person_1.get_full_name())
print(person_1.get_total_income())


