from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QCheckBox, QListWidget # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from .widgets.smallWidgets import inputValue, messageDialog, buttonMainMenu
from constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
from datetime import datetime
import sys

# QMainWindow: E um widget de janela
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nameEdit = None
        self.cpfEdit = None
        self.errorMessage = None
        self.priority = None
        self.list = [] # Lista de pessoa pra exibir
        
        self.setWindowTitle("Fila de atendimento")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    def showMainMenu(self):
        
        CENTER = Qt.AlignmentFlag.AlignCenter

        widget = QWidget()
        layout = QVBoxLayout()

        # Adiciona uma pessoa na lista
        button_add_person = buttonMainMenu("Adicionar uma pessoa na fila")
        button_add_person.clicked.connect(self.showInputPerson)
        
        # Atende uma pessoa da lista
        button_meet_person = buttonMainMenu("Atender uma pessoa da fila")
        button_meet_person.clicked.connect(self.showMeetPerson)
        
        # Vizualia lista
        button_view_queue = buttonMainMenu("Vizualizar fila de atendimento")
        button_view_queue.clicked.connect(self.showViewQueue if len(self.list) > 0 else self.messageDialogQueueEmpty)
        
        # Faz uma denuncia
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.showReport)

        layout.addWidget(button_add_person, alignment=CENTER)
        layout.addWidget(button_meet_person, alignment=CENTER)
        layout.addWidget(button_view_queue, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout)

        self.setCentralWidget(widget)  # Atualiza o widget central


    def showInputPerson(self):
        # Limpa os dados do add anterior
        self.name = None
        self.cpf = None

        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        widget = QWidget()
        layout = QGridLayout()
        layout.setContentsMargins(10,0,10,20)

        # Recebo o widget e um manager do input
        nameInput, self.nameEdit = inputValue("Nome", "Digite o seu nome")
        cpfInput, self.cpfEdit = inputValue("CPF", "Digite o seu CPF")
        self.priority = QCheckBox("Pessoa com prioridade")

        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(150, 40)
        button_back.clicked.connect(self.showMainMenu)

        button_find = QPushButton("Enviar")
        button_find.setFont(FONT)
        button_find.setFixedSize(150, 40)
        button_find.clicked.connect(self.showMessageDialog)

        # Cria um novo QLabel sempre que chamar showInputPerson
        self.errorLabel = QLabel(self.errorMessage)
        FONT_error = QFont("Arial")
        FONT_error.setPixelSize(20)
        self.errorLabel.setFont(FONT_error)
        self.errorLabel.setStyleSheet("color: red;")

        # Adicionado componentes no layout
        layout.addWidget(nameInput, 0, 0, 1, 3)
        layout.addWidget(cpfInput, 1, 0, 1, 3)
        layout.addWidget(self.priority, 2,0)
        layout.addWidget(button_back, 3, 0)
        layout.addWidget(button_find, 3, 2)
        layout.addWidget(self.errorLabel, 4, 0, 1, 3)

        widget.setLayout(layout)
        self.setCentralWidget(widget)  # Atualiza o widget central

    # Salva informacoes se os dados forem validos
    def saveState(self) -> dict:
        if self.errorLabel is not None:
            nome = (self.nameEdit.text() if self.nameEdit else "")
            cpf = (self.cpfEdit.text() if self.cpfEdit else "")
            priority = (self.priority.isChecked() if self.priority else "")
            
            if not nome or not cpf:
                self.errorLabel.setText("Digite dados válidos")
                return {} # informacoes invalidas
            
            self.errorLabel.setText("")
            return {"nome":nome, "cpf":cpf, "prio":priority, "date":datetime.now()}
        
        return {} # Erro inesperado
    
    def showMessageDialog(self, cheked=False):
        personData = self.saveState()     
        if personData != {}:   
            messageDialog(self, "Adicionou pessoa", f"{personData}")
            self.list.append(personData["nome"])
            self.showMainMenu() # Chama o menu principal denovo
            
    def showMeetPerson(self):
        if len(self.list) > 0:
            person = self.list.pop()
            messageDialog(self, "Pessoa atendida", f"{person}")
        else:
            self.messageDialogQueueEmpty()        
    
    def showReport(self):
        # Se a lista tiver vazia deixa sair
        if len(self.list) <= 0:
            sys.exit()
        else:
            messageDialog(self, "Alerta", "Ainda tem pessoa na lista")
    
    def showViewQueue(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(16)

        widget = QWidget()
        layout = QHBoxLayout()

        # Lista
        list_widget = QListWidget()
        list_widget.addItems(self.list)
        list_widget.setFont(FONT)
        list_widget.setSpacing(8)

        # Botão só com seta
        button_back = QPushButton()
        button_back.setFixedSize(50, 280)
        from PySide6.QtWidgets import QStyle
        button_back.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowBack))
        button_back.clicked.connect(self.showMainMenu)

        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(list_widget)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def messageDialogQueueEmpty(self):
        messageDialog(self, "Alerta", "Sem pessoas na lista")