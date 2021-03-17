from Models.Entidade import Entidade
from dataclasses import dataclass

#classe Terra e suas propriedades
@dataclass
class Terra(Entidade):
    #Definição das propriedades da Terra
    nutrientes: ''
    tipo: ''
    minerais: ''
    