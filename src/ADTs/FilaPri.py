from ADTs.Node import node
#Implementação do ADT Fila
class fila:
    #Dois marcadores, início e fim, além de um contador de quantidade
    def __init__(self):
        self.begin = node(None)
        self.end = node(None)
        self.quant = 0

    def percorrer(self):
        nomes = []
        aux = self.begin
        while aux.next != None:
            nomes.append(aux.next.p.nome)
            aux.next = aux.next.next
        return nomes

    def incluir(self, p): #Método que recebe uma pessoa, criar um nó e adiciona ao fim da fila
        n = node(p)
        if self.quant == 0:
            self.begin.next = n
            self.end.next = n
        else:
            self.end.next.next = n
            self.end.next = n
        self.quant+=1

    def atender(self): #Método que atende e retorna a pessoa no início da fila
        aux = self.begin.next
        if self.quant == 1:
            self.begin.next = None
            self.end.next = None
        else:
            self.begin.next = self.begin.next.next
        self.quant -= 1
        return aux.p

    def empty(self): #Retorna se a fila tá vazia
        if self.quant == 0:
            return True
        else:
            return False