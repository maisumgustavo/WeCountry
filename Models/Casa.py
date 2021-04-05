import Entidade
import dataclasses

@dataclasses
class Casa(Entidade):
    comprimento: int
    largura: int
    altura: int
    porta: int
    janela: int
    comodo: int
    andar: int
    