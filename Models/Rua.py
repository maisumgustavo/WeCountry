import dataclasses
import Entidade

@dataclasses
class Rua(Entidade):
    
    nome: str
    extensao: int
