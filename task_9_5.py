class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Инструмент: {self.title} - пишем текст')


class Pencil(Stationery):
    def draw(self):
        print(f'Инструмент: {self.title} - рисуем')


class Handle(Stationery):
    def draw(self):
        print(f'Инструмент: {self.title} - создаем пометки')


my_pen = Pen('Ручка')
my_pen.draw()

my_pencil = Pencil('Карандаш')
my_pencil.draw()

my_handle = Handle('Маркер')
my_handle.draw()
