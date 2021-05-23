from Entidade import Entidade


class Rua(Entidade):
    def __init__(self, nome, extensao):
        super().__init__()

        self.nome = nome
        self.extensao = extensao


