class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}!')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость!')
        else:
            print(f'Скорость {self.name}  составляет {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость!')
        else:
            print(f'Скорость {self.name}  составляет {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


my_kia = TownCar(61, 'Green', 'KIA RIO', False)
print(f'Авто:{my_kia.name} | Цвет:{my_kia.color} | Скорость:{my_kia.speed}')
my_kia.go()
my_kia.turn('направо')
my_kia.stop()
my_kia.show_speed()

swat_car = PoliceCar(180, 'Black', 'Ford Mustang', True)
print(f'Авто:{swat_car.name} | Цвет:{swat_car.color} | Скорость:{swat_car.speed}')
swat_car.go()
swat_car.turn('направо')
swat_car.stop()
swat_car.show_speed()
