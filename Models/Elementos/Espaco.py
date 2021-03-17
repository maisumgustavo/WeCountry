from Models.Entidade import Entidade
from dataclasses import dataclass

@dataclass
class Espaco(Entidade):

    comprimento: int
    largura: int
    altura: int