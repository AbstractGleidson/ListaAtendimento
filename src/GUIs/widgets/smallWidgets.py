from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QMessageBox, QPushButton
from PySide6.QtGui import QFont

def inputValue(message: str, hint: str):
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


def messageDialog(parent, title, message: str, icon=QMessageBox.Icon.Information):
       messageBox = QMessageBox(parent)
       messageBox.setWindowTitle(title)
       messageBox.setText(message)
       messageBox.setIcon(icon)
       messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
       messageBox.exec()


def buttonMainMenu(message: str) -> QPushButton:
        FONT = QFont("Arial")
        FONT.setPixelSize(30)
       
        button = QPushButton(message)
        button.setFont(FONT)
        button.setFixedSize(580, 60)
        return button