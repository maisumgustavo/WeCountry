from datetime import datetime
from Models.Entidade import Entidade

teste = Entidade(1, datetime.now())
print(teste.id)