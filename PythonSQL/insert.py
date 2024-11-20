import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1305",
        database="erp"
    )
    print("Cliente inserido com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro: {err}")

mycursor = mydb.cursor()

cliente = 'Jessica'
telefone = '(99)9999-9999'
cidade = 'São Paulo'

sql = "INSERT INTO cliente (Nome, Telefone, Cidade) VALUES (%s, %s, %s)"
val = (cliente, telefone, cidade)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "registro(s) Inserido(s)")