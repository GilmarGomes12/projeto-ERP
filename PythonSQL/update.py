import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1305",
        database="erp"
    )
    print("Update bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro: {err}")

mycursor = mydb.cursor()

Nome =  'Jessica'
telefone = '(21)91234-5678'
cidade =   'Rio de Janeiro'
idcliente = '6'

sql = "UPDATE cliente SET Nome = %s, telefone = %s, Cidade = %s WHERE IdCliente = %s"
val = (Nome, telefone, cidade, idcliente)

try:
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro(s) atualizado(s)")
except mysql.connector.Error as err:
    print(f"Erro: {err}")