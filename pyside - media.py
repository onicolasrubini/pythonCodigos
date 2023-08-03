from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
from PySide6.QtCore import QSize,Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("mediadasnotas.com.br")
        self.setFixedSize(1000,700)
      
        self.label1 = QLabel("Nota 1:", self)
        self.label1.setGeometry(10,10,80,30)      
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        self.label2 = QLabel("Nota 2:", self)
        self.label2.setGeometry(10,50,80,30)      
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.label3 = QLabel("Nota 3:", self)
        self.label3.setGeometry(10,90,80,30) 
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100,90,80,30)
        
        self.label4 = QLabel("Nota 4:", self)
        self.label4.setGeometry(10,130,80,30)
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100,130,80,30)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,170,280,30)
        
        self.button = QPushButton("Calcular",self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.media)
        
        
    def media(self):
        nota1 = float(self.input1.text())
        nota2 = float(self.input2.text())
        nota3 = float(self.input3.text())
        nota4 = float(self.input4.text())
        media = (nota1 + nota2 + nota3 + nota4) /4
        self.result_label.setText(f"A media dos notas é {media}")
        
             
app = QApplication(sys.argv)
janelaTwo = MainWindow()
janelaTwo.show()
app.exec()