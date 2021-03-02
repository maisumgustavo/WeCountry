from Models.Entidade import Entidade


class Animal(Entidade):
    def __init__(self, qntPernas, temCalda):
        self.qntPernas = qntPernas
        self.temCalda = temCalda

    qntPernas = int
    temCalda = bool