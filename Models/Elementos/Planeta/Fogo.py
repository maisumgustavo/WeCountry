from Models.Entidade import Entidade
from dataclasses import dataclass


#classe Terra e suas propriedades
@dataclass
class Fogo(Entidade):
    #Definição das propriedades do Fogo
    temperatura = float
    combustivel = bool
    volume = int
    