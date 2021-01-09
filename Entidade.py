class Entidade:

    def __init__(self, id):
        self.id = int(input())

    def __int__(self):
        return self.id

entidade = Entidade(1)
print(entidade.id)