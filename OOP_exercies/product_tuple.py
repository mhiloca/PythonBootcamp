def decor(n):
    print('- ' * n)


class Bill(list):
    def __init__(self):
        super().__init__()
        while True:
            decor(5)
            self.append(Product())
            while True:
                ans = input('Would you like to register another product? ').strip().upper()[0]
                if ans not in 'NY':
                    print('\033[31mInvalid answer\033[m')
                else:
                    break
            if ans == 'N':
                break

    def __repr__(self):
        return super().__repr__()

    def table(self):
        decor(18)
        print(f'{"PRICE LIST":^36}')
        decor(18)
        for i in self:
            print(f'{i.name:.<28}${i.price:>5}')


class Product:
    def __init__(self):
        self.name = input('Product name: ').title()
        while True:
            self.price = input('Product price: ')
            try:
                self.price = float(self.price.replace(',', '.'))
                break
            except ValueError:
                print('\033[31mInvalid amount\033[m')

    def __repr__(self):
        return f'{self.name} - ${self.price}'


final_bill = Bill()
final_bill.table()
