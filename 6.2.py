class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        m1kvm = int(input('Введите массу, необходимую для покрытия 1 кв.м.'))
        sm = int(input('Введите толщину асфальта'))
        print(f'Необходимая масса асфальта - {int(self._length) * int(self._width) * m1kvm * sm}')


road_1 = Road(5, 6)
road_1.mass()
