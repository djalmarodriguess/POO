#Classe pai
class Empregados:

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def trabalho(self):
        print(f'{self.nome} trabalha com...')


#Classe filha pode ter suas proprias funções.
class DataEngineer(Empregados):

    def __init__(self, nome, idade, salario, nivel):
        super().__init__(nome, idade, salario)    #Comando super faz referência aos paramêtros da classe pai
        self.nivel = nivel
    

class Designer(Empregados):
    pass

p1 = DataEngineer('Djalma', 26, 3000, 'Junior')
print(p1.nome, p1.idade)    
p1.trabalho()
print(p1.nivel)

d1 = Designer('Felipe', 32, 5000)
print(d1.nome, d1.idade)
d1.trabalho()

#output
#Djalma 26
#Djalma trabalha com...
#Junior
#Felipe 32
#Felipe trabalha com...