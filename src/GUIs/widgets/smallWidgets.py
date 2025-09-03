# Alguns componentes pequenos que nao precisao da estar na classe principal de GUIs
# como botoes personalizados e entradas
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QMessageBox, QPushButton
from PySide6.QtGui import QFont


# Prompt de entrada com uma caixa de texto e uma label
# indicando o conteudo que deve ser inserido na caixa de texto
def inputValue(message: str, hint: str):
        # Fonte personalizada
        FONT = QFont("Arial")
        FONT.setPixelSize(20)

        # Texto 
        label = QLabel(message)
        label.setFont(FONT)
        label.setFixedHeight(20)  # trava a altura

        # Caixa de texto
        inputDialog = QLineEdit()
        inputDialog.setPlaceholderText(hint)
        inputDialog.setFixedSize(580, 40) # trava o tamanho da caixa de texto

        # Layout para adicionar os componentes
        # Vai adicionando um widget em baixo
        layout = QVBoxLayout()
        layout.setSpacing(2)  # controla espaço entre label e input
        layout.setContentsMargins(0, 0, 0, 0)

        # Adiciona o texto e caixa de texto no layout
        layout.addWidget(label)
        layout.addWidget(inputDialog)

        # Cria um widget generico
        widget = QWidget()  
        widget.setLayout(layout) # Adiciona o layout junto com oque tem dentro do layout no widget
        # retorna o widget e a caixa de texto
        # precisa retornar a caixa de texto para acessar oque foi escrito dentro dela
        return widget, inputDialog 


# Cria uma janela de dialog pequena com apenas uma messagem
def messageDialog(parent, title, message: str, icon=QMessageBox.Icon.Information):
       messageBox = QMessageBox(parent) # Janela de dialogo
       messageBox.setWindowTitle(title)
       messageBox.setText(message)
       messageBox.setIcon(icon)
       messageBox.setStandardButtons(QMessageBox.StandardButton.Ok) # Adiciona o botao padrao pra dar ok
       messageBox.exec() # Executa essa janela por cima de qualquer outra

# Botao de menu com o tamanho ideal para o menu da janela principal
def buttonMainMenu(message: str) -> QPushButton:
        FONT = QFont("Arial")
        FONT.setPixelSize(30)
       
        button = QPushButton(message)
        button.setFont(FONT)
        button.setFixedSize(580, 60)
        return button # retorna o botao