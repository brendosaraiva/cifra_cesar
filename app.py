import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criptografia de Cesar")
        self.setFixedSize(700, 467)
        self.interface()

    def interface(self):
        self.label = QLabel(self)
        self.original_pixmap = QPixmap("images/soldado_romano_mensageiro.png")
        if self.original_pixmap.isNull():
            print("Erro: Imagem não encontrada ou inválida.")
        self.label.setPixmap(self.original_pixmap)
        self.label.resize(self.size())  # Define o tamanho inicial
        self.label.setScaledContents(False)

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