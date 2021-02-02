from .Ser_Humano import Ser_Humano

class Homem(Ser_Humano):
    
    def __init__(self, Cabeca, Braco_Direito, Braco_Esquerdo, Tronco, Perna_Direita, Perna_Esquerda):
    self.Cabeca = Cabeca
    self.Braco_Direito = Braco_Direito
    self.Braco_Esquerdo = Braco_Esquerdo
    self.Tronco = Tronco
    self.Perna_Esquerda = Perna_Esquerda
    self.Perna_Direita = Perna_Direita

Fernando = Homem(True, True, True, True, True, True)
print(Fernando)