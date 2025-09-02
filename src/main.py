from GUIs.MyApp import MyWindow
from PySide6.QtWidgets import QApplication 
import sys

if __name__ == "__main__":
    app = QApplication()
    myWindow = MyWindow()
    myWindow.show() # Exibe a janela principal
    sys.exit(app.exec())