from Models.Entidade import Entidade

class Espaco(Entidade):
    def __init__(self, comprimento, largura, altura):
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    comprimento = int
    largura = int
    altura = int