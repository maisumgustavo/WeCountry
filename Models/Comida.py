from Entidade import Entidade
from dataclasses import dataclass

@dataclass
class Comida(Entidade):
    eComida: bool

