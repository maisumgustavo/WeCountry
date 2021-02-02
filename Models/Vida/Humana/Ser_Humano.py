class Ser_Humano:
    #Espaco = Espaco
    #Vida = Vida
    #Estagio_da_Vida = Estagio_da_Vida
    Cabeca = bool
    Braco_Direito = bool
    Braco_Esquerdo = bool
    Tronco = bool
    Perna_Direita = bool
    Perna_Esquerda = bool

    def __init__(self, Cabeca, Braco_Direito, Braco_Esquerdo, Tronco, Perna_Direita, Perna_Esquerda):
        self.Cabeca = Cabeca
        self.Braco_Direito = Braco_Direito
        self.Braco_Esquerdo = Braco_Esquerdo
        self.Tronco = Tronco
        self.Perna_Direita = Perna_Direita
        self.Perna_Esquerda = Perna_Esquerda

afonso = Ser_Humano(True, True, True, True, True, True)
print(afonso)