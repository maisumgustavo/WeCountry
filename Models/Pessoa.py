from Entidade import Entidade


class Pessoa(Entidade):
    def __init__(self, nome, sexo):
        super().__init__()

        self.nome = nome
        self.sexo = sexo
    
