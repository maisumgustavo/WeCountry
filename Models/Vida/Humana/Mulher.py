from .Humano import Humano

class Mulher(Humano):
    """
        Define a propriedade de mulher.
    """
    def __init__(self, nome):
        self.nome = nome

    nome = str