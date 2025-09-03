from GUIs.MyApp import MyWindow
from PySide6.QtWidgets import QApplication 
import sys

if __name__ == "__main__":
    # Trabalha a execucao dos widgets
    # Renderiza apenas um widget por janela
    app = QApplication() 
    
    myWindow = MyWindow() # Janela principal
    myWindow.show() # Exibe a janela principal
    sys.exit(app.exec()) # Para a execucao do programa