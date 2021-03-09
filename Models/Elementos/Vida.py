from datetime import datetime
from Models.Entidade import Entidade

class Vida(Entidade):
    """
        Define a propriedade de vida para um objeto
    """
    def __init__(self, existeVida):
        self.existeVita = existeVida

    existeVita = bool

vida = Vida(True)
print(vida.existeVita)