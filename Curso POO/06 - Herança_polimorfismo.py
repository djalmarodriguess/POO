#Classe pai
class Empregados:

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def trabalho(self):
        print(f'{self.nome} trabalha com codigos...')

#Classe filha substituida, com um registro a mais do que do classe pai/base
class DataEngineer(Empregados):

    def __init__(self, nome, idade, salario, nivel):
        super().__init__(nome, idade, salario)
        self.nivel = nivel
    

class Designer(Empregados):  
    pass
    

#Lista de empregados 
empregados = [
    DataEngineer('Djalma', 26, 3000, 'Junior'),
    DataEngineer('José', 28, 6000, 'Pleno'),
    Designer('Felipe', 32, 5000)
]


def motiva_empregados(empregados):
    for i in empregados:
        i.trabalho()


motiva_empregados(empregados)

    #output
#Djalma trabalha com codigos...
#José trabalha com codigos...
#Felipe trabalha com codigos...


#Anotações
#Herança 
#Herdar, estender, substituir (inherit, exteder, override)
#super.__init__()
#Polimorfismo