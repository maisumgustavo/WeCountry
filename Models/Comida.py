from Entidade import Entidade

class Comida(Entidade):
    def __init__(self, eComida):
        self.eComida = eComida
        self.id = Entidade.id
        self.data_Criacao = Entidade.data_Criacao

    eComida = bool

comida = Comida(True)
print(comida.id)
print(comida.data_Criacao)