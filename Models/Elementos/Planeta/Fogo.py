from Models.Entidade import Entidade


#classe Terra e suas propriedades
class Fogo(Entidade):
    """
        Definição das propriedades do Fogo
    """
    def __init__(self, temperatura, combustivel, volume):
        self.temperatura = temperatura
        self.combustivel = combustivel
        self.volume = volume

    temperatura = float
    combustivel = bool
    volume = int