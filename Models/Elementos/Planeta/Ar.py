from Models.Entidade import Entidade

#classe Ar e suas propriedades
class Ar(Entidade):
    #Definição das propriedades do Ar
    def __init__(self, sabor, cheiro, volume, massa):
        self.sabor = sabor
        self.cheiro = cheiro
        self.volume = volume
        self.massa = massa

    sabor = bool
    cheiro = bool
    volume = int
    massa = int