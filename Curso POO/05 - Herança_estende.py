#Classe pai
class Empregados:

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


#Classe filha pode ter suas proprias funções.
class DataEngineer(Empregados):

    def dados(self):
        print(f'{self.nome} trabalha com codigos...')


class Designer(Empregados):
        
    def desenho(self):
        print(f'{self.nome} trabalha com desenho...')



p1 = DataEngineer('Djalma', 26, 3000)
p1.dados()

d1 = Designer('Felipe', 32, 5000)
d1.desenho()



    #output
#Djalma trabalha com codigos...
#Felipe trabalha com desenho...
