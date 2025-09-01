import sys 
from constants import WINDOW_WIDTH, WINDOW_HEIGTH, X_POSITION, Y_POSITION, ICON2_PATH
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

# Cria a janela principal
class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Atendimento") # Define um titulo para a janela
        self.setGeometry(X_POSITION, Y_POSITION, WINDOW_WIDTH, WINDOW_HEIGTH) # Define a posicao de criacao da janela e o tamanho
        self.setWindowIcon(QIcon(ICON2_PATH))
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
       
        
        button1 = QPushButton("Opção 1", self)
        button1.setGeometry(0, 0, WINDOW_WIDTH, 100)
        button1.setStyleSheet("font-size: 30px;")
        button1.clicked.connect(self.on_click) # Funcao que vai executar quando o botao for clikado
        
        button2 = QPushButton("Opção 2", self)
        button2.setGeometry(0, 0, WINDOW_WIDTH, 100)
        button2.setStyleSheet("font-size: 30px;")
        button2.clicked.connect(self.on_click) # Funcao que vai executar quando o botao for clikado
        
        button3 = QPushButton("Opção 3", self)
        button3.setGeometry(0, 0, WINDOW_WIDTH, 100)
        button3.setStyleSheet("font-size: 30px;")
        button3.clicked.connect(self.on_click) # Funcao que vai executar quando o botao for clikado
        
        button4 = QPushButton("Opção 4", self)
        button4.setGeometry(0, 0, WINDOW_WIDTH, 100)
        button4.setStyleSheet("font-size: 30px;")
        button4.clicked.connect(self.on_click) # Funcao que vai executar quando o botao for clikado
        
        # Layout
        Vbox = QVBoxLayout()
        
        Vbox.addWidget(button1)
        Vbox.addWidget(button2)
        Vbox.addWidget(button3)
        Vbox.addWidget(button4)
        
        central_widget.setLayout(Vbox)
        
    
    def on_click(self):
        print("Fui clicado!")

def createWindow():
    app =  QApplication(sys.argv) # Cria a janela
    window = MainMenuWindow()
    window.show()
    sys.exit(app.exec_())