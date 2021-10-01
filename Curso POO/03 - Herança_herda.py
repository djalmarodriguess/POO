#herda, estende, substitui
class Empregados:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def trabalho(self):
        print(f'{self.nome} trabalha com...')

class DataEngineer(Empregados):
    pass
class Designer(Empregados):
    pass

p1 = DataEngineer('Djalma', 26)
print(p1.nome, p1.idade)
p1.trabalho()

d1 = Designer('Felipe', 32)
print(d1.nome, d1.idade)

