from pathlib import Path

# Tamanho da janela
WINDOW_WIDTH = 300 # Vertical
WINDOW_HEIGTH = 600 # Horizontal

# Posicao inicial da janela
X_POSITION = 0 # Eixo horizotal
Y_POSITION = 0 # Eixo vertical

# Pega a origen do projeto e sobe uma pasta
BASE_DIR = Path(__file__).resolve().parents[1]  

#Caminho do arquivo
ICON1_PATH = str(BASE_DIR / "assets" / "icon1.png")
ICON2_PATH = str(BASE_DIR / "assets" / "icon2.png")