from Models.Entidade import Entidade

class Espaco(Entidade):
    """
        Determina um espaço disponivel ou não disponivel.
        Esse espação é 3 dimensões, ou seja: comprimento, largura e altura.
    """
    def __init__(self, comprimento, largura, altura):
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    comprimento = int
    largura = int
    altura = int