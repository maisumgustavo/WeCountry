from Models.Entidade import Entidade
from dataclasses import dataclass

@dataclass
class Luz(Entidade):

    radiacao_Infravermelha: bool
    radiacao_Ultravioleta: bool
    frequencia: int
    temperatura: float
    lumen: int
