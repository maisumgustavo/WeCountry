from Models.Entidade import Entidade
from Models.Elementos.Espaco import Espaco
from dataclasses import dataclass
#classe água e suas propriedades

@dataclass
class Agua(Entidade, Espaco):
    Sabor: bool
    Cheiro: bool
    Volume: Espaco

