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
        self.idadeTotal = 0
    
    def cadastra(self, nome, cpf, idade, prio): #Método que cria uma pessoa e a adiciona a pilha designada (prioritária ou não)
        cliente = pessoa(nome, cpf, idade)
        self.idadeTotal += idade
        if prio == 1:
            self.atendidosp += 1
            self.filap.incluir(cliente)
        else:
            self.atendidosnp += 1
            self.filanp.incluir(cliente)
        return (f"{cliente.nome} cadastrado(a) com sucesso às {cliente.dateFormat()}")
    
    def atende(self) -> pessoa | None: #Retorna a próxima pessoa atendida, usando de contadores de atendimento para organizar a ordem.
        if self.filap.empty() & self.filanp.empty():
            return None

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
    
    def pessoas_na_fila(self): #Retorna uma tupla que contém dois arrays de nomes, prioritários e não-prioritários
        return (self.filap.percorrer(),self.filanp.percorrer())
    
    def queue_empty(self): #Retorna se as filas estão vazias para poder fechar o programa
        return self.filap.empty() and self.filanp.empty()
    
    def registro(self): #Estatísticas exibidas ao fim do programa
        total = self.atendidosp+self.atendidosnp
        if(total == 0):
            return f"Ninguém foi atendido"
        else:
            if(total > 1):
                return (f"Foram atendidas {total} pessoas, com uma faixa etária média de {self.idadeTotal/total:.1f} anos.\n {self.atendidosp} eram prioritárias. ( {(self.atendidosp*100)/total:.2f}%) \n {self.atendidosnp} eram não-prioritárias. ( {(self.atendidosnp*100)/total:.2f}%)")
            else:
                return (f"Foi atendido {total} pessoa, com a faixa etária de {self.idadeTotal} anos.\n{self.atendidosp} era prioritária. ( {(self.atendidosp*100)/total:.2f}%) \n{self.atendidosnp} era não-prioritária. ( {(self.atendidosnp*100)/total:.2f}%)")