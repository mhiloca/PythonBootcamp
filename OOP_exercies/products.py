def decor(n):
    print('- ' * n)


class Bill(list):
    def __init__(self):
        super().__init__()
        while True:
            decor(5)
            self.append(Product())
            while True:
                ans = input('Register another product? ').strip().upper()[0]
                if ans not in 'NY':
                    print('\033[31mInvalid answer\033[m')
                else:
                    break
            if ans == 'N':
                break


class Product:
    def __init__(self):
        self.name = input('Product name: ').title()
        while True:
            self.price = input('Product price: ')
            try:
                self.price = float(self.price.replace(',', '.'))
                break
            except ValueError:
                print('\033[31mInvalid price\033[m')

    def __repr__(self):
        return f'{self.name} - ${self.price}'


class Total:
    def __init__(self, bill):
        self.bill = bill
        decor(15)
        print(self._total())
        decor(5)
        self._expensives()
        decor(5)
        print(self._cheapest())

    def _total(self):
        return f'Purchase total: ${sum(map(lambda x: x.price, self.bill))}'

    def _expensives(self):
        for i in self.bill:
            if i.price > 1000:
                print(i)

    def _cheapest(self):
        return f'The cheapeast product is {min(self.bill, key=lambda x: x.price)}'


final_bill = Bill()
Total(final_bill)
