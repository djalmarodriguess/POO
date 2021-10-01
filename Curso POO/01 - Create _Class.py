'''
Classes são usadas para estrutura de dados mais complexas, que contém 
funções que descrevem a hierarquia das classes,
então classe é como se fosse um diagrama de como alguma coisa deve ser definida.
'''

#Class
class Profissao():
    
    #Atributo class
    apelido = "Peão de Obra"

    def __init__(self, nome, idade, nivel, salario):   #Descrevemos que queremos na classe.
        #Atributos da instancia
        self.nome = nome
        self.idade = idade
        self.nivel = nivel
        self.salario = salario


#Instancia da class
p1 = Profissao('Djalma', 26, 'Junior', 2000)
p2 = Profissao('José', 28, 'Pleno', 6000) 
print(p1.nome, p1.salario)
print(Profissao.apelido)
print(p2.nome, p2.idade)


#output's
#Djalma 2000
#Peão de Obra
#José 28


#Anotação
#Criação da classe (diagrama)
#Criação das instancias (Objetos)
#Atributos da instancia: definidos em __init__(self)
#Atributo classe


