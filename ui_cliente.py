# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(740, 566)
        self.bt_cliente = QPushButton(Form)
        self.bt_cliente.setObjectName(u"bt_cliente")
        self.bt_cliente.setGeometry(QRect(10, 0, 81, 71))
        self.bt_cliente.setMinimumSize(QSize(60, 30))
        self.bt_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/adicionar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cliente.setIcon(icon)
        self.bt_cliente.setIconSize(QSize(60, 60))
        self.bt_cliente_2 = QPushButton(Form)
        self.bt_cliente_2.setObjectName(u"bt_cliente_2")
        self.bt_cliente_2.setGeometry(QRect(90, 0, 81, 71))
        self.bt_cliente_2.setMinimumSize(QSize(60, 30))
        self.bt_cliente_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/alterar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cliente_2.setIcon(icon1)
        self.bt_cliente_2.setIconSize(QSize(60, 60))
        self.bt_cliente_3 = QPushButton(Form)
        self.bt_cliente_3.setObjectName(u"bt_cliente_3")
        self.bt_cliente_3.setGeometry(QRect(170, 0, 81, 71))
        self.bt_cliente_3.setMinimumSize(QSize(60, 30))
        self.bt_cliente_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/consultar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cliente_3.setIcon(icon2)
        self.bt_cliente_3.setIconSize(QSize(60, 60))
        self.bt_cliente_4 = QPushButton(Form)
        self.bt_cliente_4.setObjectName(u"bt_cliente_4")
        self.bt_cliente_4.setGeometry(QRect(250, 0, 81, 71))
        self.bt_cliente_4.setMinimumSize(QSize(60, 30))
        self.bt_cliente_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cliente_4.setIcon(icon3)
        self.bt_cliente_4.setIconSize(QSize(60, 60))
        self.bt_cliente_5 = QPushButton(Form)
        self.bt_cliente_5.setObjectName(u"bt_cliente_5")
        self.bt_cliente_5.setGeometry(QRect(650, 0, 81, 71))
        self.bt_cliente_5.setMinimumSize(QSize(60, 30))
        self.bt_cliente_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/retornar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cliente_5.setIcon(icon4)
        self.bt_cliente_5.setIconSize(QSize(60, 60))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 170, 721, 371))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 120, 51, 30))
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/pesquisar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(30, 30))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 121, 30))
        self.label.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 120, 461, 30))
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(670, 120, 51, 30))
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/filtro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bt_cliente.setText("")
        self.bt_cliente_2.setText("")
        self.bt_cliente_3.setText("")
        self.bt_cliente_4.setText("")
        self.bt_cliente_5.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Telefone", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Cidade", None));
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Nome Cliente:", None))
        self.pushButton_2.setText("")
    # retranslateUi

