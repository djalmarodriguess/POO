class DataEngineer():

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self._salario = None             #Valor protegido (identificado por 1 underscore)
        self._num_bugs_resolvidos = 0    #Valor protegido (identificado por 1 underscore)

    #Função para visualizar o valor que está em self._salario - getter
    def ver_salario(self):
        return self._salario

    #Função para adicionar um salario a instancia self._salario - setter
    def inserir_salario(self, valor):
        self._salario = self._soma_salario(valor)

    def codigo(self):
        self._num_bugs_resolvidos += 1

    def _soma_salario(self, valor):
        if self._num_bugs_resolvidos < 10:
            return valor
        if self._num_bugs_resolvidos < 100:
            return valor * 2
        return valor * 3
    

p1 = DataEngineer('Djalma', 26)
print(p1.nome, p1.idade)


for i in range(70):
    p1.codigo()

p1.inserir_salario(6000)
print(p1.ver_salario())

#output
#Djalma 26
#12000