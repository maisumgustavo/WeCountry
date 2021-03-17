from Models.Entidade import Entidade
from dataclasses import dataclass

@dataclass
class Animal(Entidade):
    qntPernas: int
    temCalda: bool