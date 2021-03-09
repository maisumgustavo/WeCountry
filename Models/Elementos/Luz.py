from Models.Entidade import Entidade


class Luz(Entidade):
    """
        Define uma propriedade luminosa.
    """
    def __init__(self, radiacao_Infravermelha, raiacao_Ultravioleta, frequencia, temperatura, lumen):
        self.radiacao_Infravermelha = radiacao_Infravermelha
        self.radiacao_Ultravioleta = raiacao_Ultravioleta
        self.frequencia = frequencia
        self.temperatura = temperatura
        self.lumen = lumen

    radiacao_Infravermelha = bool
    radiacao_Ultravioleta = bool
    frequencia = int
    temperatura = float
    lumen = int
