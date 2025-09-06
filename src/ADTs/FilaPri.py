from ADTs.Node import node

class fila:
    def __init__(self):
        self.begin = node(None)  # Sentinela
        self.end = node(None)    # Guarda o último em end.next
        self.quant = 0

    def percorrer(self): # Percorre a fila, retornando um array que contém os nomes de todas as pessoas atualmente nela
        nomes = []
        aux = self.begin.next
        while aux is not None:
            nomes.append(aux.p.nome)
            aux = aux.next
        return nomes

    def incluir(self, p): # Cria um nó n, com uma pessoa p e o adiciona na fila
        n = node(p)
        if self.quant == 0:
            self.begin.next = n
            self.end.next = n
        else:
            self.end.next.next = n
            self.end.next = n
        self.quant += 1

    def atender(self): # Atende a pessoa na frente da fila, retirando e retornando quem foi atendido
        if self.quant == 0:
            return None  # ou: raise IndexError("fila vazia")
        aux = self.begin.next
        if self.quant == 1:
            self.begin.next = None
            self.end.next = None
        else:
            self.begin.next = aux.next
        self.quant -= 1
        return aux.p

    def empty(self): # Retorna se a fila está vazia ou não
        return self.quant == 0
