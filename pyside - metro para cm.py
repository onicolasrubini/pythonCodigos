from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("exerciciocinco.com.br")
        self.setGeometry(100,100,300,150)
      
        self.label = QLabel("Número:", self)
        self.label.setGeometry(10,10,80,30)
        self.input = QLineEdit(self)
        self.input.setGeometry(100,10,80,30)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        
        self.button = QPushButton("Calcular",self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.metros_cm)
        
        
    def metros_cm(self):
        num = int(self.input.text())
        cm = num * 100
        self.result_label.setText(f"{cm} cm")
        
      
app = QApplication(sys.argv)
janelaTwo = MainWindow()
janelaTwo.show()
app.exec()