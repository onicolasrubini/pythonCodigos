from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import logn_img


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"porsche.com.br")
        MainWindow.resize(1035, 748)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")   
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_principal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_usuario = QFrame(self.frame_principal)
        self.frame_usuario.setObjectName(u"frame_usuario")
        self.frame_usuario.setFrameShape(QFrame.StyledPanel)
        self.frame_usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_usuario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.imagem = QLabel(self.frame_usuario)
        self.imagem.setObjectName(u"imagem")
        self.imagem.setPixmap(QPixmap(u"../../Downloads/porsche-normal.jpg"))
        self.imagem.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.imagem)

        self.lbl_usuario = QLabel(self.frame_usuario)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        font = QFont()
        font.setPointSize(15)
        self.lbl_usuario.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_usuario)

        self.input_usuario = QLineEdit(self.frame_usuario)
        self.input_usuario.setObjectName(u"input_usuario")

        self.verticalLayout_2.addWidget(self.input_usuario)

        self.verticalLayout_3.addWidget(self.frame_usuario)

        self.frame_senha = QFrame(self.frame_principal)
        self.frame_senha.setObjectName(u"frame_senha")
        self.frame_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_senha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_senha = QLabel(self.frame_senha)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setFont(font)

        self.verticalLayout.addWidget(self.lbl_senha)

        self.input_senha = QLineEdit(self.frame_senha)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.input_senha)

        self.verticalLayout_3.addWidget(self.frame_senha)

        self.verticalLayout_4.addWidget(self.frame_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imagem.setText("")
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.input_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe seu nome", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    janela = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(janela)
    janela.show()
    app.exec()