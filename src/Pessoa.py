from datetime import datetime
#Classe que representa uma pessoa a ser atendida
class pessoa: 
    #Contém nome, cpf (strings) e Datas de chegada e atendimento
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.chegada = datetime.now()
        self.atendido = 0
    

    def __str__(self):
        return(f"{self.nome}")
    

