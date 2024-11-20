# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dadosCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


### Imports sistema ###
import mysql.connector
import pandas as pd

### Arquivo variáveis de controle ###
import variaveisControle

### Variáveis de conexão com o banco de dados ###
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database



class Ui_formDadosCliente(object):
    def setupUi(self, formDadosCliente):
        formDadosCliente.setObjectName("formDadosCliente")
        formDadosCliente.resize(361, 249)
        self.lb_nome = QtWidgets.QLabel(formDadosCliente)
        self.lb_nome.setGeometry(QtCore.QRect(30, 50, 49, 21))
        self.lb_nome.setObjectName("lb_nome")
        self.txt_nome = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_nome.setEnabled(True)
        self.txt_nome.setGeometry(QtCore.QRect(90, 50, 221, 21))
        self.txt_nome.setText("")
        self.txt_nome.setObjectName("txt_nome")
        self.lb_telefone = QtWidgets.QLabel(formDadosCliente)
        self.lb_telefone.setGeometry(QtCore.QRect(28, 90, 51, 21))
        self.lb_telefone.setObjectName("lb_telefone")
        self.txt_telefone = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_telefone.setGeometry(QtCore.QRect(90, 90, 221, 21))
        self.txt_telefone.setText("")
        self.txt_telefone.setObjectName("txt_telefone")
        self.lb_cidade = QtWidgets.QLabel(formDadosCliente)
        self.lb_cidade.setGeometry(QtCore.QRect(30, 130, 49, 21))
        self.lb_cidade.setObjectName("lb_cidade")
        self.txt_cidade = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_cidade.setGeometry(QtCore.QRect(90, 130, 221, 21))
        self.txt_cidade.setText("")
        self.txt_cidade.setObjectName("txt_cidade")
        self.bt_cancelar = QtWidgets.QPushButton(formDadosCliente)
        self.bt_cancelar.setGeometry(QtCore.QRect(100, 170, 81, 51))
        self.bt_cancelar.setStyleSheet("image: url(:/icon_cancelar/Icons/cancelar.png)")
        self.bt_cancelar.setText("")
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.bt_cadastrar = QtWidgets.QPushButton(formDadosCliente)
        self.bt_cadastrar.setGeometry(QtCore.QRect(200, 170, 81, 51))
        self.bt_cadastrar.setStyleSheet("image: url(:/icon_cadastrar/Icons/cadastrar.png)")
        self.bt_cadastrar.setText("")
        self.bt_cadastrar.setObjectName("bt_cadastrar")

        self.retranslateUi(formDadosCliente)
        QtCore.QMetaObject.connectSlotsByName(formDadosCliente)

    def retranslateUi(self, formDadosCliente):
        _translate = QtCore.QCoreApplication.translate
        formDadosCliente.setWindowTitle(_translate("formDadosCliente", "Form"))
        self.lb_nome.setText(_translate("formDadosCliente", "Nome:"))
        self.lb_telefone.setText(_translate("formDadosCliente", "Telefone:"))
        self.lb_cidade.setText(_translate("formDadosCliente", "Cidade:"))
        self.bt_cancelar.setToolTip(_translate("formDadosCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_cadastrar.setToolTip(_translate("formDadosCliente", "<html><head/><body><p><br/></p></body></html>"))

        ### Botões sistema ###
        self.bt_cancelar.clicked.connect(lambda: self.sairTela(formDadosCliente))
        if variaveisControle.tipoTelaDadosCliente == 'incluir':
            self.bt_cadastrar.clicked.connect(self.cadastrarCliente)
        if variaveisControle.tipoTelaDadosCliente == 'alterar':
            self.bt_cadastrar.clicked.connect(self.alterarCliente)

        ### Condições da tela ###
        ## Tipo form tela ##
        if variaveisControle.tipoTelaDadosCliente == 'incluir':
            print('dadosCliente: ', variaveisControle.tipoTelaDadosCliente)
            self.txt_nome.setEnabled(True)
            self.txt_telefone.setEnabled(True)
            self.txt_cidade.setEnabled(True)
            self.bt_cadastrar.setEnabled(True)
        elif variaveisControle.tipoTelaDadosCliente == 'consultar':
            print('dadosCliente: ', variaveisControle.tipoTelaDadosCliente)
            self.txt_nome.setEnabled(False)
            self.txt_telefone.setEnabled(False)
            self.txt_cidade.setEnabled(False)
            self.bt_cadastrar.setEnabled(False)
            # Conexão com o banco de dados #
            mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
            mycursor = mydb.cursor()
            consultaSQL = "SELECT * FROM cliente WHERE IdCliente = '" + variaveisControle.idConsulta + "'"
            mycursor.execute(consultaSQL)
            myresult = mycursor.fetchall()
            mycursor.close()
            # Converte resultados BD para DataFrame #
            df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
            nomeCliente = df['Nome'][0]
            telefoneCliente = df['Telefone'][0]
            cidadeCliente = df['Cidade'][0]
            # Seta variáveis na tela do sistema #
            self.txt_nome.setText(nomeCliente)
            self.txt_telefone.setText(telefoneCliente)
            self.txt_cidade.setText(cidadeCliente)
        elif variaveisControle.tipoTelaDadosCliente == 'alterar':
            print('dadosCliente: ', variaveisControle.tipoTelaDadosCliente)
            self.txt_nome.setEnabled(True)
            self.txt_telefone.setEnabled(True)
            self.txt_cidade.setEnabled(True)
            self.bt_cadastrar.setEnabled(True)
            # Conexão com o banco de dados #
            mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
            mycursor = mydb.cursor()
            consultaSQL = "SELECT * FROM cliente WHERE IdCliente = '" + variaveisControle.idConsulta + "'"
            mycursor.execute(consultaSQL)
            myresult = mycursor.fetchall()
            mycursor.close()
            # Converte resultados BD para DataFrame #
            df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
            nomeCliente = df['Nome'][0]
            telefoneCliente = df['Telefone'][0]
            cidadeCliente = df['Cidade'][0]
            # Seta variáveis na tela do sistema #
            self.txt_nome.setText(nomeCliente)
            self.txt_telefone.setText(telefoneCliente)
            self.txt_cidade.setText(cidadeCliente)


    ### FUNÇÕES SISTEMA ###
    ## Sair dadosCliente ##
    def sairTela(self, formDadosCliente):
        variaveisControle.tipoTelaDadosCliente == ''
        formDadosCliente.close()

    ## CADASTRAR CLIENTE ##
    def cadastrarCliente(self):
        nomeCliente = self.txt_nome.text()
        telefoneCliente = self.txt_telefone.text()
        cidadeCliente = self.txt_cidade.text()

        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO cliente (Nome, Telefone, Cidade) values (%s,  %s, %s)"
        val = (nomeCliente, telefoneCliente, cidadeCliente)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, 'record(s) inserted')
        mycursor.close()
        self.txt_nome.setText("")
        self.txt_telefone.setText("")
        self.txt_cidade.setText("")

    ## ALTERAR CLIENTE ##
    def alterarCliente(self):
        nomeCliente = self.txt_nome.text()
        telefoneCliente = self.txt_telefone.text()
        cidadeCliente = self.txt_cidade.text()

        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        mycursor = mydb.cursor()
        sql = "UPDATE cliente SET Nome = '" + nomeCliente + "', Telefone = '" + telefoneCliente + "', Cidade = '" + cidadeCliente + "' WHERE IdCliente = '" + variaveisControle.idConsulta + "'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, 'record(s) altered')
        mycursor.close()





### Imagens Sistema ###
import icon_cadastrar
import icon_cancelar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formDadosCliente = QtWidgets.QWidget()
    ui = Ui_formDadosCliente()
    ui.setupUi(formDadosCliente)
    formDadosCliente.show()
    sys.exit(app.exec_())