from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QCheckBox, QListWidget # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from constants import ICON2_PATH

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
        self.setFixedSize(600, 300)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela

    def buttonMainMenu(self, message: str) -> QPushButton:
        FONT = QFont("Arial")
        FONT.setPixelSize(30)
       
        button = QPushButton(message)
        button.setFont(FONT)
        button.setFixedSize(580, 60)
        return button

    def showMainMenu(self):
        
        CENTER = Qt.AlignmentFlag.AlignCenter

        widget = QWidget()
        layout = QVBoxLayout()

        # Adiciona uma pessoa na lista
        button_add_person = self.buttonMainMenu("Adicionar uma pessoa na fila")
        button_add_person.clicked.connect(self.showInputPerson)
        
        # Atende uma pessoa da lista
        button_meet_person = self.buttonMainMenu("Atender uma pessoa da fila")
        button_meet_person.clicked.connect(self.showMeetPerson)
        
        # Vizualia lista
        button_view_queue = self.buttonMainMenu("Vizualizar fila de atendimento")
        button_view_queue.clicked.connect(self.showViewQueue)
        
        # Faz uma denuncia
        button_report = self.buttonMainMenu("Registrar denuncia")
        button_report.clicked.connect(self.showReport)

        layout.addWidget(button_add_person, alignment=CENTER)
        layout.addWidget(button_meet_person, alignment=CENTER)
        layout.addWidget(button_view_queue, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout)

        self.setCentralWidget(widget)  # Atualiza o widget central
    
    def inputValue(self, message: str, hint: str):
        FONT = QFont("Arial")
        FONT.setPixelSize(20)

        label = QLabel(message)
        label.setFont(FONT)
        label.setFixedHeight(20)  # trava a altura

        inputDialog = QLineEdit()
        inputDialog.setPlaceholderText(hint)
        inputDialog.setFixedSize(580, 40)
        
        layout = QVBoxLayout()
        layout.setSpacing(2)  # controla espaço entre label e input
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(label)
        layout.addWidget(inputDialog)

        widget = QWidget()
        widget.setLayout(layout)
        return widget, inputDialog


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
        nameInput, self.nameEdit = self.inputValue("Nome", "Digite o seu nome")
        cpfInput, self.cpfEdit = self.inputValue("CPF", "Digite o seu CPF")
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

        
    def messageDialog(self, message: str):
       messageBox = QMessageBox(self)
       messageBox.setWindowTitle("Sucesso")
       messageBox.setText(message)
       messageBox.setIcon(QMessageBox.Icon.Information)
       messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
       messageBox.exec()
       
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
            return {"nome":nome, "cpf":cpf, "prio":priority}
        
        return {} # Erro inesperado
    
    def showMessageDialog(self, cheked=False):
        personData = self.saveState()     
        if personData != {}:   
            self.messageDialog(f"{personData}")
            self.showMainMenu() # Chama o menu principal denovo
            
    def showMeetPerson(self):
        pass            
    
    def showReport(self):
        pass
    
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
        button_back.setFixedWidth(390)
        button_back.setFixedSize(50, 40)
        from PySide6.QtWidgets import QStyle
        button_back.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowBack))
        button_back.clicked.connect(self.showMainMenu)

        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(list_widget)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)