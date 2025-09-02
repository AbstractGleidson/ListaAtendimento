import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PyQt5.QtGui import QIcon
from constants import ICON2_PATH
from .screens.main_menu_window import main_menu_window
from .screens.add_person_window import add_person_window
from .screens.show_messager_dialog import show_messager_dialog

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Sistema de Atendimento")
        self.setGeometry(100, 100, 800, 400)
        self.setWindowIcon(QIcon(ICON2_PATH))

        # Stacked Widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # --- Instanciando as interfaces ---
        self.menu_ui = main_menu_window()
        self.add_person_ui = add_person_window()
        self.message_ui = show_messager_dialog()

        # --- Criando widgets QMainWindow para cada UI ---
        self.menu_window = QMainWindow()
        self.menu_ui.setupUi(self.menu_window)

        self.add_person_window = QMainWindow()
        self.add_person_ui.setupUi(self.add_person_window)

        self.message_window = QMainWindow()
        self.message_ui.setupUi(self.message_window)

        # --- Adicionando ao stack ---
        self.stack.addWidget(self.menu_window)
        self.stack.addWidget(self.add_person_window)
        self.stack.addWidget(self.message_window)

        # Página inicial
        self.stack.setCurrentWidget(self.menu_window)

        # --- Conectar botões ---
        self.menu_ui.pushButton.clicked.connect(self.goto_add_person)
        self.add_person_ui.pushButton.clicked.connect(self.send_person)
        self.add_person_ui.pushButton_2.clicked.connect(self.goto_menu)
        self.message_ui.pushButton.clicked.connect(self.goto_menu)

    # --- Métodos de navegação ---
    def goto_add_person(self):
        self.stack.setCurrentWidget(self.add_person_window)

    def goto_menu(self):
        self.stack.setCurrentWidget(self.menu_window)

    def send_person(self):
        nome = self.add_person_ui.lineEdit.text()
        cpf = self.add_person_ui.lineEdit_2.text()
        prioridade = self.add_person_ui.checkBox.isChecked()
        print(f"Pessoa adicionada: {nome}, CPF: {cpf}, Prioridade: {prioridade}")
        
        # Atualiza mensagem
        self.message_ui.label.setText(f"Foi adicionada à fila: {nome}")
        
        # Vai para a tela de mensagem
        self.stack.setCurrentWidget(self.message_window)

def createWindow():
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
