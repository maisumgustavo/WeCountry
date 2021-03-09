from Models.Entidade import Entidade
from Models.Comida import Comida


class Humano(Entidade, Comida):
    """
        Define a propriedade de ser humano.
    """
    Id = Entidade.id
    eComida = Comida.eComida
    Cabeca = bool
    Braco_Direito = bool
    Mao_Direita = bool
    Braco_Esquerdo = bool
    Mao_Esquerda = bool
    Tronco = bool
    Perna_Direita = bool
    Pe_Direito = bool
    Perna_Esquerda = bool
    Pe_Esquerdo = bool

    def __init__(self, Cabeca, Braco_Direito, Braco_Esquerdo, Tronco, Perna_Direita, Perna_Esquerda):
        super().__init__()
        self.Cabeca = Cabeca
        self.Braco_Direito = Braco_Direito
        self.Braco_Esquerdo = Braco_Esquerdo
        self.Tronco = Tronco
        self.Perna_Direita = Perna_Direita
        self.Perna_Esquerda = Perna_Esquerda
        self.data_Criacao = Entidade.data_Criacao

Humano = Humano(True, True, True, True, True, True)
print(Humano.id)
print(Humano.Data_criacao)
print(Humano.eComida)