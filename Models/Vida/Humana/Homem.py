import Humano

class Homem(Humano):
    """
        Nomeia um ser humano.
    """
    def __init__(self, nome):
        self.nome = nome

    nome = str

homem = Homem(str)
print(homem.Cabeca)