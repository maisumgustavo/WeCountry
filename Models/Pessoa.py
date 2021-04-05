import Entidade
import dataclasses

@dataclasses
class Pessoa(Entidade):
    nome: str
    sexo: bool
    