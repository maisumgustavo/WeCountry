from .. import Entidade

class Estagio_da_Vida(Entidade):
    def __init__(self, eRacional, fome, sede):
        self.eRacional = eRacional
        self.fome = fome
        self.sede = sede

    eRacional = bool
    fome = float
    sede = float