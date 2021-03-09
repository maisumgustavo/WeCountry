import datetime
from dataclasses import dataclass


@dataclass
class Entidade():
    """
        Classe de onde tudo se herda.
        Nela tema identificação e data de criação de todos os objetos.
    """
    id: int
    data_Criacao: datetime

entidade = Entidade(1, datetime.datetime.now())

print(entidade.data_Criacao)