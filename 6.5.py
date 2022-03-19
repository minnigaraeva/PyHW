class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('hybrid')


class Pencil(Stationery):
    def draw(self):
        print('mellow')


class Handle(Stationery):
    def draw(self):
        print('owwwww')


pen = Pen('brauberg')
pencil = Pencil('HBB')
handle = Handle('Soft')
pen.draw()
pencil.draw()
handle.draw()
print(pen.title)
