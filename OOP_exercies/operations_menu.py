class Num:
    def __init__(self):
        while True:
            try:
                self.num = int(input('Valor: '))
                break
            except ValueError:
                print('\033[31mValor inválido\033[m')

    def __repr__(self):
        return self.num


class Operations:
    def __init__(self, n1, n2):
        while True:
            try:
                self.opt = int(input('Escolha a operação:\n'
                                     '[ 1 ] Somar\n'
                                     '[ 2 ] Multiplicar\n'
                                     '[ 3 ] Maior\n'
                                     '[ 4 ] Novos números\n'
                                     '[ 5 ] Sair do programa\n'
                                     'Digite a opção: '))
                if not 1 <= self.opt <= 5:
                    print('\033[31mOpção inválida\033[m')
                else:
                    break
            except ValueError:
                print('\033[31mOpção inválida\033[m')
        print('- ' * 10)
        self.n1 = n1.num
        self.n2 = n2.num

    def _somar(self):
        return self.n1 + self.n2

    def _mult(self):
        return self.n1 * self.n2

    def _maior(self):
        return max(self.n1, self.n2)

    def _novos(self):
        self.n1 = Num()
        self.n2 = Num()
        return Operations(self.n1, self.n2).res()

    def res(self):
        if self.opt == 1:
            return f'{self.n1} + {self.n2} = {self._somar()}'
        elif self.opt == 2:
            return f'{self.n1} x {self.n2} = {self._mult()}'
        elif self.opt == 3:
            return f'O maior número é {self._maior()}'
        elif self.opt == 4:
            return self._novos()
        return 'FINALIZANDO OPERAÇÕES'


numero1 = Num()
numero2 = Num()
oper = Operations(numero1, numero2)
print(oper.res())
