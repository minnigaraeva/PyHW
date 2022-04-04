class OfficeEquipmentWarehouse:
    def __init__(self):
        self.contents = {}
        self.rmv = {}

    def __str__(self):
        return f'{self.contents}'

    def take_items(self):
        try:
            for i in range(len(OfficeEquipment.giving)):
                self.contents[OfficeEquipment.giving[i]] = int(input('Number of items'))
        except ValueError:
            print('Need a number')


class OfficeEquipment:
    giving = []

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def give(self):
        self.giving.append(self.brand + ' ' + self.model)


class Printer(OfficeEquipment):
    def __init__(self, brand, model, print_type='laser'):
        super().__init__(brand, model)
        self.print_type = print_type


class Scaner(OfficeEquipment):
    def __init__(self, brand, model, streaming=False):
        super().__init__(brand, model)
        self.streaming = streaming


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, colorful=True):
        super().__init__(brand, model)
        self.colorful = colorful


xerox = Xerox('hp', '2w56')
scaner = Scaner('mi', '4+')
printer = Printer('canon', '6h')
warehouse = OfficeEquipmentWarehouse()
xerox.give()
scaner.give()
warehouse.take_items()
print(warehouse)
