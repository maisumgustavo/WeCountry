from datetime import datetime
from ..Entidade import Entidade

class Vida(Entidade):
    def __init__(self, existeVida):
        self.existeVita = existeVida
        self.data_Criacao = datetime.now()

    existeVita = bool
    data_Criacao = datetime

vida = Vida(True)
print(vida.existeVita)
print(vida.data_Criacao)