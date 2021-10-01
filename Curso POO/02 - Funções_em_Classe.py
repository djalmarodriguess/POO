'''
Classe são muito mais estruturais que lista.
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

    #Metodo instancia
    def code(self):
        print(f'{self.nome} está codificando...')

    def code_na_linguagem(self, linguagem):
        print(f'{self.nome} está codificando na linguagem {linguagem}...')


    #Dunder method
    def __str__(self):   #Tranforma uma função em string.
        informacao = f'nome = {self.nome}, idade = {self.idade}, nivel = {self.nivel}, salario = {self.salario}'
        return informacao

    def __eq__(self, object):   #Coparação do endereço de memoria caso não seja informado os itens de comparação
        return self.nome == object.nome and self.idade == object.idade   #Necessario informar o que deseja comparar 
                                                                         #Será comparado nome e idade, se é FALSE ou TRUE

    @staticmethod
    def entra_salario(idade):     #Possivel fazer uma mudança no registro de acordo com a descrição da função.
        if idade < 25:
            return 5000
        if idade < 30:
            return 7000
        return 9000


#Instancia
p1 = Profissao('Djalma', 26, 'Junior', 2000)
p2 = Profissao('José', 28, 'Pleno', 6000) 
p3 = Profissao('José', 28, 'Pleno', 6000) 


p1.code()
p2.code_na_linguagem('Python')
p1.code_na_linguagem('Java')
print(p1)
print(p2 == p3)
print(p1.entra_salario(40))
print(Profissao.entra_salario(24))

#output's
#Djalma está codificando...
#José está codificando na linguagem Python...
#Djalma está codificando na linguagem Java...
#nome = Djalma, idade = 26, nivel = Junior, salario = 2000
#True
#9000
#5000

#Anotação
#Metodo instancia
#return valores
#Dunder method (__str__ e __eq__)
#@staticmethod