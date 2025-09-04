from Pessoa import pessoa
#Classe que representa um nó, contando um next e uma pessoa
class node:
    def __init__(self, p):
        self.p = p
        self.next = None