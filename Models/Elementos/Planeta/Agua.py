
#classe água e suas propriedades

class Agua:
    #Definição das propriedades da água
    def __init__(self, sabor, cheiro, volume):
        self.Sabor = sabor
        self.Cheiro = cheiro
        self.Volume = volume

    Sabor = bool
    Cheiro = bool
    Volume = int

agua = Agua(True, True, 10)
print(agua.Sabor)
print(agua.Volume)
print(agua.Cheiro)