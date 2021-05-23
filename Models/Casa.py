from Entidade import Entidade

class Casa(Entidade):
    def __init__(self, comprimento, largura, altura):
        super().__init__()

        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura
        self.porta = 1
        self.janela = 1
        self.comodo = 1
        self.andar = 1
    
   
casa = Casa(100, 101, 102)