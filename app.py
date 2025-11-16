import os

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6 import QtCore

from criptografia import criptografar
from descriptografia import descriptografar


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criptografia de Cesar")
        self.setFixedSize(700, 467)
        self.setWindowIcon(QIcon("images/icone_do_sistema"))
        self.setWindowOpacity(0.90)
        self.interface()

    def metodo(self):
        # Escreve o conteúdo no arquivo
        with open("log/mensagem.txt", mode="w", encoding="utf-8") as arquivo:
            arquivo.write(self.texto.toPlainText())

        # Lê o conteúdo em um bloco separado
        with open("log/mensagem.txt", mode="r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().split()

            # criptografar ou descriptografar
            if self.criptografar_msg.isChecked():
                criptografar(conteudo)
            else:
                descriptografar(conteudo)

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
        argumentos.setFont(QFont("Times New Roman", 14))
        argumentos.setStyleSheet("color: white; font-style: negrito;")
        argumentos.move(280, 275)

        # Método que o sistema irá empregar (criptografia/descriptografia)
        self.criptografar_msg = QRadioButton("Criptografar:", self)
        self.criptografar_msg.setStyleSheet("color: white; background-color: none;")
        self.criptografar_msg.move(250, 390)
        self.criptografar_msg.setChecked(True)
        self.descriptografar_msg = QRadioButton("Descriptografar:", self)
        self.descriptografar_msg.setStyleSheet("color: white; background-color: none;")
        self.descriptografar_msg.move(350, 390)

        # Enviar mensagem
        botao1 = QPushButton("Submeter", self)
        botao1.setStyleSheet("color: white; background-color: gray;")
        botao1.move(320, 420)
        botao1.clicked.connect(self.metodo)

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
