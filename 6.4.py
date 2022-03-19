class Car:
    def __init__(self, speed, color, name, is_police=False, direction=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Too high speed!')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Too high speed!')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


work_car = WorkCar(50, 'black', 'Volga', False)
town = TownCar(50, 'white', 'Vaz2112', False)
sport = SportCar(180, 'green', 'Audi', False)
police = PoliceCar(150, 'white', 'Mercedes', True)
work_car.go()
town.stop()
sport.show_speed()
police.turn('направо')
town.show_speed()
work_car.show_speed()
