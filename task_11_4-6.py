class Stock:

    def __init__(self, max_volume, sum_volume=0):
        self.max_volume = max_volume
        self.nomenclature = {'printers': {}, 'scanners': {}, 'copiers': {}}
        self.sum_volume = sum_volume

    def __str__(self):
        return str(self.nomenclature)

    def shipment(self, of_equipment, brand, quantity, departament):
        if self.nomenclature.get(of_equipment.lower()).get(brand.lower()):
            if self.nomenclature.get(of_equipment.lower()).get(brand.lower()) >= quantity:
                self.nomenclature.get(of_equipment)[brand.lower()] = self.nomenclature.get(of_equipment.lower()).get(
                    brand.lower()) - quantity
                if departament.stock.get(of_equipment.lower()).get(brand.lower()):
                    departament.stock.get(of_equipment.lower())[brand.lower()] = departament.stock.get(
                        of_equipment.lower()).get(
                        brand.lower()) + quantity
                else:
                    departament.stock.get(of_equipment.lower()).setdefault(brand.lower(), quantity)

            else:
                print(f'There are only {self.nomenclature.get(of_equipment).get(brand)} {brand} left to stock!')

        else:
            print(f'No {brand} in stock!')


class OfficeEquipment:
    brand_volume = {}
    name = 'Equipment'

    def __init__(self, brand, value):
        try:
            self.value = int(value)
        except ValueError as err:
            print(err)
            self.value = int(input('Enter quantity: '))
        self.brand = brand

    @classmethod
    def volume(cls, self):
        return self.value * cls.brand_volume.get(self.brand.lower())

    def arrival(self, name_stock):
        if (name_stock.sum_volume + self.volume(self)) < name_stock.max_volume:
            name_stock.sum_volume += self.volume(self)
            if name_stock.nomenclature.get(self.name).get(self.brand.lower()):
                name_stock.nomenclature.get(self.name)[self.brand.lower()] = name_stock.nomenclature.get(
                    self.name).get(
                    self.brand.lower()) + self.value
            else:
                name_stock.nomenclature.get(self.name).setdefault(self.brand.lower(), self.value)

        else:
            print(f'Stock is full. Remaining volume: {name_stock.max_volume - name_stock.sum_volume}')


class Printer(OfficeEquipment):
    brand_volume = {'xerox': 1.4, 'hp': 0.9, 'canon': 0.8, 'kyocera': 2.1}

    def __init__(self, brand, value, p_type='jet', name='printers'):
        if brand.lower() in Printer.brand_volume:
            super().__init__(brand, value)
        else:
            Printer.brand_volume[brand.lower()] = input('Please enter volume this mark: ')
            self.brand = brand
        self.p_type = p_type
        self.name = name


class Scanner(OfficeEquipment):
    brand_volume = {'brother': 0.6, 'fujitsu': 0.5, 'canon': 0.4, 'epson': 0.2}

    def __init__(self, brand, value, s_type='flatbed', name='scanners'):
        if brand.lower() in Scanner.brand_volume:
            super().__init__(brand, value)
        else:
            Scanner.brand_volume[brand.lower()] = input('Please enter volume this mark: ')
            self.brand = brand
        self.p_type = s_type
        self.name = name


class Copier(OfficeEquipment):
    brand_volume = {'brother': 0.4, 'fujitsu': 0.7, 'canon': 0.3, 'epson': 0.6}

    def __init__(self, brand, value, c_type='А4', name='copiers'):
        if brand.lower() in Scanner.brand_volume:
            super().__init__(brand, value)
        else:
            Scanner.brand_volume[brand.lower()] = input('Please enter volume this mark: ')
            self.brand = brand
        self.p_type = c_type
        self.name = name


class Departament:
    def __init__(self):
        self.stock = {'printers': {}, 'scanners': {}, 'copiers': {}}

    def __str__(self):
        return str(self.stock)


class ItDep(Departament):
    pass


class SaleDep(Departament):
    pass


class AccountDep(Departament):
    pass


my_stock = Stock(100)
my_sale_dep = SaleDep()

consignment_1 = Printer('xerox', 30, 'lazer')
consignment_2 = Scanner('brother', 20)
consignment_3 = Copier('canon', 10)

consignment_1.arrival(my_stock)
consignment_2.arrival(my_stock)
consignment_3.arrival(my_stock)

print(my_stock)

my_stock.shipment('printers', 'xerox', 10, my_sale_dep)
my_stock.shipment('scanners', 'brother', 10, my_sale_dep)
my_stock.shipment('copiers', 'canon', 10, my_sale_dep)

print(my_sale_dep)
print(my_stock)
