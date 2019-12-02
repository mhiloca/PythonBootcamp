from functools import wraps


def decor(n):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print('- ' * n)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@decor(15)
def title(msg):
    print(f'{msg:^30}')
    print('- ' * 15)


class Pessoa:
    @decor(5)
    def __init__(self):
        self.nome = input('Nome: ').title()
        self.sobrenome = input('Sobrenome: ').title()
        while True:
            try:
                self.idade = int(input('Idade: '))
                break
            except ValueError:
                print('\033[31mIdade inválida\033[m')
        generos = ('mulher-cis', 'homem-cis', 'mulher-trans',
                   'homem-trans', 'não-binário')
        while True:
            print(generos)
            self.gen = input('Gênero: ').strip().lower()
            if self.gen not in generos:
                print('\033[31mGênero inválido\033[m')
            else:
                break

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Analista:
    def __init__(self, cad):
        self.cad = cad

    @decor(20)
    def media_idade(self):
        soma = sum(map(lambda x: x.idade, self.cad))
        media = soma / len(self.cad)
        return f'A média de idade das pessoas cadastradas é {round(media, 1)} anos'


    @decor(20)
    def max_mulher(self):
        mulheres = filter(lambda x: x.gen == 'mulher-cis' or x.gen == 'mulher-trans', self.cad)
        return f'A mulher mais velha é {max(mulheres, key=lambda x: x.idade).nome_completo()}'

    @decor(20)
    def min_homens(self):
        homens = list(
            filter(
                lambda x: x.idade < 20 and x.gen == 'homem-trans' or x.gen == 'homem-cis' and x.idade < 20, self.cad
            )
        )
        return f'A quantidade de homens menores de 20 anos é {len(homens)}'


cadastro = []
for i in range(3):
    title(f'PESSOA {i+1}')
    cadastro.append(Pessoa())
analise = Analista(cadastro)
print(analise.max_mulher())
print(analise.media_idade())
print(analise.min_homens())
