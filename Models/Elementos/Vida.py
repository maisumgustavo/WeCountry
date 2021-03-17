from datetime import datetime
from Models.Entidade import Entidade
from dataclasses import dataclass

@dataclass
class Vida(Entidade):
    existeVita: bool

vida = Vida(True)
print(vida.existeVita)