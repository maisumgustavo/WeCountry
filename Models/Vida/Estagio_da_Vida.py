from .. import Entidade

class Estagio_da_Vida(Entidade):
    """
        Classe que define um estágia de vida de um objeto baseado em sua data de criação.
    """
    def __init__(self, eRacional, fome, sede):
        self.eRacional = eRacional
        self.fome = fome
        self.sede = sede

    eRacional = bool
    fome = float
    sede = float