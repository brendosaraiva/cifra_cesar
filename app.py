import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6 import QtCore


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criptografia de Cesar")
        self.setFixedSize(700, 467)
        self.setWindowIcon(QIcon("images/icone_do_sistema"))
        self.setWindowOpacity(0.90)
        self.interface()

    def interface(self):
        self.label = QLabel(self)
        self.original_pixmap = QPixmap("images/soldado_romano_mensageiro.png")
        if self.original_pixmap.isNull():
            print("Erro: Imagem não encontrada ou inválida.")
        self.label.setPixmap(self.original_pixmap)
        self.label.resize(self.size())  # Define o tamanho inicial
        self.label.setScaledContents(False)

        # Caixa de mensagem -> Será utilizada para receber a mensagem
        self.texto = QTextEdit(self)
        self.texto.setFixedWidth(280)
        self.texto.setFixedHeight(80)
        self.texto.move(220, 300)
        argumentos = QLabel("Insira a mensagem:", self)
        argumentos.setFont(QFont("Times New Roman", 12))
        argumentos.setStyleSheet("color: white; font-style: negrito;")
        argumentos.move(220, 280)

        # Método que o sistema irá empregar (criptografia/descriptografia)
        self.seleciona_tema1 = QRadioButton("Criptografar:", self)
        self.seleciona_tema1.setStyleSheet("color: white; background-color: none;")
        self.seleciona_tema1.move(220, 390)
        self.seleciona_tema1.setChecked(True)
        self.seleciona_tema2 = QRadioButton("Descriptografar:", self)
        self.seleciona_tema2.setStyleSheet("color: white; background-color: none;")
        self.seleciona_tema2.move(320, 390)

    def resizeEvent(self, event):
        if hasattr(self, 'original_pixmap') and not self.original_pixmap.isNull():
            scaled = self.original_pixmap.scaled(
                self.label.size(),
                QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                QtCore.Qt.TransformationMode.SmoothTransformation
            )
            self.label.setPixmap(scaled)
        super().resizeEvent(event)

app = QApplication(sys.argv)
janela = JanelaPrincipal()
janela.show()
sys.exit(app.exec())