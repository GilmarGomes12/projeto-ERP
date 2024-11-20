# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dadoscliente.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import icon_rc

class Ui_FormDadosCliente(object):
    def setupUi(self, FormDadosCliente):
        if not FormDadosCliente.objectName():
            FormDadosCliente.setObjectName(u"FormDadosCliente")
        FormDadosCliente.resize(508, 295)
        self.lb_nome = QLabel(FormDadosCliente)
        self.lb_nome.setObjectName(u"lb_nome")
        self.lb_nome.setGeometry(QRect(24, 50, 71, 30))
        self.lb_nome.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lb_nome.setFont(font)
        self.bl_telefone = QLabel(FormDadosCliente)
        self.bl_telefone.setObjectName(u"bl_telefone")
        self.bl_telefone.setGeometry(QRect(20, 100, 101, 30))
        self.bl_telefone.setMinimumSize(QSize(0, 30))
        self.bl_telefone.setFont(font)
        self.lb_cidade = QLabel(FormDadosCliente)
        self.lb_cidade.setObjectName(u"lb_cidade")
        self.lb_cidade.setGeometry(QRect(20, 150, 81, 30))
        self.lb_cidade.setMinimumSize(QSize(0, 30))
        self.lb_cidade.setFont(font)
        self.txt_nome = QLineEdit(FormDadosCliente)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setEnabled(True)
        self.txt_nome.setGeometry(QRect(120, 50, 371, 30))
        self.txt_nome.setMinimumSize(QSize(0, 30))
        self.txt_telefone = QLineEdit(FormDadosCliente)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(120, 100, 371, 30))
        self.txt_telefone.setMinimumSize(QSize(0, 30))
        self.txt_cidade = QLineEdit(FormDadosCliente)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(120, 150, 371, 30))
        self.txt_cidade.setMinimumSize(QSize(0, 30))
        self.bt_cancelar = QPushButton(FormDadosCliente)
        self.bt_cancelar.setObjectName(u"bt_cancelar")
        self.bt_cancelar.setGeometry(QRect(140, 200, 91, 71))
        self.bt_cancelar.setMinimumSize(QSize(70, 30))
        self.bt_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cancelar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cancelar.setIcon(icon)
        self.bt_cancelar.setIconSize(QSize(60, 60))
        self.bt_cadastrar = QPushButton(FormDadosCliente)
        self.bt_cadastrar.setObjectName(u"bt_cadastrar")
        self.bt_cadastrar.setGeometry(QRect(260, 200, 91, 71))
        self.bt_cadastrar.setMinimumSize(QSize(70, 30))
        self.bt_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cadastrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cadastrar.setIcon(icon1)
        self.bt_cadastrar.setIconSize(QSize(60, 60))

        self.retranslateUi(FormDadosCliente)

        QMetaObject.connectSlotsByName(FormDadosCliente)
    # setupUi

    def retranslateUi(self, FormDadosCliente):
        FormDadosCliente.setWindowTitle(QCoreApplication.translate("FormDadosCliente", u"Form", None))
        self.lb_nome.setText(QCoreApplication.translate("FormDadosCliente", u"Nome:", None))
        self.bl_telefone.setText(QCoreApplication.translate("FormDadosCliente", u"Telefone:", None))
        self.lb_cidade.setText(QCoreApplication.translate("FormDadosCliente", u"Cidade:", None))
        self.bt_cancelar.setText("")
        self.bt_cadastrar.setText("")
    # retranslateUi

