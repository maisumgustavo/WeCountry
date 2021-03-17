from Models.Entidade import Entidade
from dataclasses import dataclass
#classe Ar e suas propriedades

@dataclass
class Ar(Entidade):
    #Definição das propriedades do Ar
    sabor: bool
    cheiro: bool
    volume: int
    massa: int
