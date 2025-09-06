# Cria de fato a interface da aplicacao
# Para futuras modificacao, e interessante implementar um esquema de navegacao usando QStackedWidget
from PySide6.QtWidgets import QMainWindow, QWidget, QCheckBox, QListWidget, QStyle # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from .widgets.smallWidgets import inputValue, messageDialog, buttonMainMenu
from constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
#from datetime import datetime
import sys
from ADTs.Manager import queueManager

# Herda QMainWindow para ter acesso a alguns componentes da janela em si, como title e icon 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nameEdit = None # Atributo que vai controlar a entrada da caixa de texto do nome
        self.cpfEdit = None # Atributo que vai controlar a entrada da caixa de texto do CPF
        self.ageEdit = None # Atributo que controla a entrada de idade
        self.errorMessage = None # Gerencia a messagem de erro na leitura de dado, se ela deve ser exibida ou nao
        self.priority = None # Atributo que controla se um pessoa tem prioridade ou nao, para direciona-la para a fila adequada
        self.queueManagerApp = queueManager() # Instancia a classe para gerenciar a fila
        
        self.setWindowTitle("Fila de atendimento")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 

        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical 

        # Adiciona uma pessoa na lista
        button_add_person = buttonMainMenu("Adicionar uma pessoa na fila")
        button_add_person.clicked.connect(self.showInputPerson) # Adiciona funcao para esse botao
        
        # Atende uma pessoa da lista
        button_meet_person = buttonMainMenu("Atender uma pessoa da fila")
        button_meet_person.clicked.connect(self.showMeetPerson) # Adiciona funcao para esse botao
        
        # Vizualia lista
        button_view_queue = buttonMainMenu("Vizualizar fila de atendimento")
        # Existe um bug que se eu acabo de esvaziar a lista eu ainda consigo chamar self.showViewQueue - Verificar isso
        button_view_queue.clicked.connect(self.showViewQueue) # Adiciona funcao para esse botao
        
        # Sai da aplicacao
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.exitAplication) # Adiciona funcao para esse botao

        # Adiciona os botoes no layout
        layout.addWidget(button_add_person, alignment=CENTER)
        layout.addWidget(button_meet_person, alignment=CENTER)
        layout.addWidget(button_view_queue, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout) # Adiciona o layout no widget generico

        self.setCentralWidget(widget)  # Renderiza esse widget generico que foi criado 


    # Renderiza a tela de entrada de dados, cadastro de uma pessoa
    def showInputPerson(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        widget = QWidget()
        layout = QGridLayout() # Cria uma layout em formato de grade(linhas e colunas)
        # 10px - Distancia para a margen esquerda
        # 0px - Distancia para o top 
        # 10px - Distancia para a margen da direita
        # 20px - Distancia para o ground ou parte de baixo da janela
        layout.setContentsMargins(10,0,10,0) # Cria uma restricao de distancia do layout e margens da janela
        

        # Recebe o widget generico e o manager para a caixa de texto
        nameInput, self.nameEdit = inputValue("Nome", "Digite o seu nome")
        cpfInput, self.cpfEdit = inputValue("CPF", "Digite o seu CPF")
        ageInput , self.ageEdit = inputValue("Idade", "Digite a sua idade")
        self.priority = QCheckBox("Pessoa com prioridade") # Caixa de marcacao

        # Cria um botao para volta para o menu
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(150, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Botao para confirmar os dados 
        button_find = QPushButton("Enviar")
        button_find.setFont(FONT)
        button_find.setFixedSize(150, 40)
        button_find.clicked.connect(self.showMessageDialog)

        # Istancia o errolabel com a messagem 
        self.errorLabel = QLabel(self.errorMessage)
        FONT_error = QFont("Arial")
        FONT_error.setPixelSize(20)
        self.errorLabel.setFont(FONT_error)
        self.errorLabel.setStyleSheet("color: red;")

        # Adicionado componentes no layout
        layout.addWidget(nameInput, 0, 0, 1, 3)
        layout.addWidget(cpfInput, 1, 0, 1, 3)
        layout.addWidget(ageInput, 2, 0, 1, 3)
        layout.addWidget(self.priority, 3,0)
        layout.addWidget(button_back, 4, 0)
        layout.addWidget(button_find, 4, 2)
        layout.addWidget(self.errorLabel, 5, 0, 1, 3)

        widget.setLayout(layout)
        self.setCentralWidget(widget)  # Renderiza 

    # Salva informacoes se os dados forem validos
    def saveState(self) -> dict:
        nome = (self.nameEdit.text() if self.nameEdit else "") # Recebe os dados da caixa de texto
        cpf = (self.cpfEdit.text() if self.cpfEdit else "") # Recebe os dados da caixa de texto
        age = (self.ageEdit.text() if self.ageEdit else "")
        priority = (self.priority.isChecked() if self.priority else "") # Recebe os dados da caixa de marcacao 
        
        # Verifica se os dados sao validos
        try:
            if len(cpf) != 11 or not cpf.isdigit():
                raise Exception("Cpf Invalido!")
            age = int(age) # tenta converter 
            if not cpf or not nome:
                raise Exception("Não digitou seus dados!")
            
            self.errorLabel.setText("") # Seta erroLabel como vazio para ele nao aparecer na tela
            return {"nome":nome, "cpf":cpf, "prio":priority, "idade": age} # retorna os dados coletados
        except:
            self.errorLabel.setText("Digite dados válidos") 
            # Se os dados nao forem validos muda o valor da label de erro
            # Ela sempre existe, mas quando nao tem erro ela e uma string vazia
            return {} # Indica que algo deu errado
        
        
    # Pequena janela para mostrar se deu certo a entrada de dados ou nao
    def showMessageDialog(self):
        personData = self.saveState() # Coleta os dados
        
        # Verifica se deu algum erro na entrada de dados
        if personData != {}:   
            response = self.queueManagerApp.cadastra(personData['nome'], personData['cpf'], personData['idade'], personData['prio'])
            messageDialog(self, "Adicionou pessoa", response)
            self.showMainMenu() # Chama o menu principal denovo
            
        # Se os dados forem invalidos, showInputPerson continua ativa, apenas mudando o valor de errorLabel
            
    # Atende uma pessoa da fila e mostra a pessoa que foi atendida
    def showMeetPerson(self):
        # Se a fila nao for vazia ele tira da fila
        if not self.queueManagerApp.queue_empty():
            response = self.queueManagerApp.atende()
            if response != None:
                messageDialog(self, "Pessoa atendida", f"{response.nome} foi atendido(a)!")
        else:
            self.messageDialogQueueEmpty() # Se a lista tiver vazia mostra messagem de erro        
    
    # Sai da aplicacao
    def exitAplication(self):
        # Se a fila tiver vazia deixa sair
        if self.queueManagerApp.queue_empty():
            messageDialog(self, "Dados da fila", self.queueManagerApp.registro())
            sys.exit()
        else:
            messageDialog(self, "Alerta", "Ainda há pessoas na fila") # Se ainda tiver alguem na fila, mostra erro
    
    # Mostra as pessoas na fila se tiver alguma pessoa na fila 
    def showViewQueue(self):
        if not self.queueManagerApp.queue_empty(): # Se tiver alguem para mostrar
            FONT = QFont("Arial")
            FONT.setPixelSize(16)

            widget = QWidget()
            layout = QHBoxLayout()

           
            
            # Instancia o widget responsavel por mostra uma lista de valores e criar um scroll
            list_widget = QListWidget()
            list_queeu = self.queueManagerApp.pessoas_na_fila()
            
            if len(list_queeu[1]) > 0:
                list_widget.addItem("---------- Pessoas sem Prioridade ----------")
                list_widget.addItems(list_queeu[1]) # Pessoas sem prioridade
            if len(list_queeu[0]) > 0:
                list_widget.addItem("---------- Pessoas com Prioridade ----------")
                list_widget.addItems(list_queeu[0]) # Pessoas com prioridade
            list_widget.setFont(FONT)
            list_widget.setSpacing(8) # Adiciona um espaco de 8px entre cada elemento

            # Botão só com seta para voltar 
            button_back = QPushButton()
            button_back.setFixedSize(50, 280)
            button_back.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowBack)) # Seta um icon padrao no botao
            button_back.clicked.connect(self.showMainMenu) # Adiciona funcao no botao

            layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignLeft)
            layout.addWidget(list_widget)
            
            widget.setLayout(layout)
            self.setCentralWidget(widget)
        else:
            self.messageDialogQueueEmpty()
        
    # Messagem de erro para fila vazia
    def messageDialogQueueEmpty(self):
        messageDialog(self, "Alerta", "Sem pessoas na lista")