from datetime import datetime
# Classe que representa uma pessoa a ser atendida
class pessoa: 
    # Contém nome, cpf (strings) e Datas de chegada e atendimento
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.chegada =  datetime.now()

    # Retorna a data formatada
    def dateFormat(self) -> str:
        return self.chegada.strftime("%H:%M %p - %d/%m/%Y") 

    def __str__(self) -> str:
        return(f"{self.nome}")
    

