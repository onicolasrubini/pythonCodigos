import sys
import brazilcep
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Cadastro")
        self.setFixedSize(900,700)
        
        layout = QVBoxLayout()
        layoutH = QHBoxLayout()
        
        #nome
        self.label_nome = QLabel("Nome:", self)
        self.label_nome.setGeometry(20,20,160,30)
        self.input_nome = QLineEdit(self)
        self.input_nome.setGeometry(80,19,160,30)

        #sexo
        self.label_sexo = QLabel("Sexo:", self)
        self.label_sexo.setGeometry(20,60,160,30)
        
        self.checkMasc = QCheckBox("M",self)
        self.checkMasc.setGeometry(80,59,90,30)
        self.checkFem = QCheckBox("F",self)
        self.checkFem.setGeometry(120,59,80,30)
        
        #print masc/fem
        layout.addWidget(self.checkMasc)
        layout.addWidget(self.checkFem)
        self.checkMasc.stateChanged.connect(self.masc)
        self.checkFem.stateChanged.connect(self.feminino)
        
        #cep
        self.label_cep = QLabel("CEP:", self)
        self.label_cep.setGeometry(20,100,160,30)
        self.input_cep = QLineEdit(self)
        self.input_cep.setGeometry(80,99,160,30)
        
        #bairro
        self.label_bairro = QLabel("Bairro:", self)
        self.label_bairro.setGeometry(20,150,160,30)
        self.input_bairro = QLineEdit(self)
        self.input_bairro.setGeometry(80,149,160,30)

        #cidade
        self.label_cidade = QLabel("Cidade:", self)
        self.label_cidade.setGeometry(20,200,160,30)
        self.input_cidade = QLineEdit(self)
        self.input_cidade.setGeometry(80,199,160,30)
        
        #rua
        self.label_rua = QLabel("Rua:", self)
        self.label_rua.setGeometry(20,250,160,30)
        self.input_rua = QLineEdit(self)
        self.input_rua.setGeometry(80,249,160,30)
        
        self.input_cep.returnPressed.connect(self.cep_automatico)
        
    def cep_automatico(self):
        cep = self.input_cep.text()
        endereco = brazilcep.get_address_from_cep(cep)
        self.input_cidade.setText(endereco['city'])
        self.input_bairro.setText(endereco['district'])
        self.input_rua.setText(endereco['street'])
    
    
    def masc(self, s):
        if s == self.checkMasc.setChecked:
            self.checkFem.setChecked(True)
            
        else:
            self.checkFem.setChecked(False)
            
            
    def feminino(self, s):
        if s == self.checkFem.setChecked:
            self.checkMasc.setChecked(True)
            
        else:
            self.checkMasc.setChecked(False)
        
        
app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()