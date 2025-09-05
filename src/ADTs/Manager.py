from ADTs.FilaPri import fila
from ADTs.Pessoa import pessoa

class queueManager:
    #Cria estruturas e contadores para controle
    def __init__(self):
        self.filap = fila()
        self.filanp = fila()
        self.p = 0
        self.np = 0
        self.atendidosp = 0
        self.atendidosnp = 0
    
    def cadastra(self, nome, cpf, prio): #Método que cria uma pessoa e a adiciona a pilha designada (prioritária ou não)
        cliente = pessoa(nome, cpf)
        if prio == 1:
            self.atendidosp += 1
            self.filap.incluir(cliente)
        else:
            self.atendidosnp += 1
            self.filanp.incluir(cliente)
        return (f"{cliente.nome} cadastrada com sucesso às {cliente.chegada}!")
    
    def atende(self) -> pessoa: #Retorna a próxima pessoa atendida, usando de contadores de atendimento para organizar a ordem.
        if self.filap.empty() & self.filanp.empty():
            return pessoa(None, None)

        elif self.filap.empty():
            self.np+=1
            return self.filanp.atender()

        elif self.filanp.empty():
            self.p+=1
            return self.filap.atender()

        else:
            if(self.np >= 2):
                self.np = 0
                self.p = 0
                
            if self.p == 0:
                self.p+=1
                return self.filap.atender()
            else:
                self.np+=1
                return self.filanp.atender()
            

    def valido(self, cpf): #Checa se uma string é um cpf válido (Tem 11 caracteres e só possui números)
        if len(cpf) != 11:
            return False
        
        for x in cpf:
            if not x.isdigit():
                return False
            
        return True
    
    def pessoas_na_fila(self):
        return (self.filap.percorrer(),self.filanp.percorrer())
    
    def queue_empty(self): #Retorna se as filas estão vazias para poder fechar o programa
        return self.filap.empty() and self.filanp.empty()
    
    def registro(self): #Estatísticas exibidas ao fim do programa
        total = self.atendidosp+self.atendidosnp
        if(total == 0):
            return f"Ninguém foi atendido"
        else:
            return (f"Foram atendidas {total} pessoas.\n {self.atendidosp} eram prioritárias. ( {(self.atendidosp*100)/total}%) \n {self.atendidosnp} eram não-prioritários. ( {(self.atendidosnp*100)/total}%)")