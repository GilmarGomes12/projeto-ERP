import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1305",
        database="erp"
    )
    print("Cliente removido!")
except mysql.connector.Error as err:
    print(f"Erro: {err}")

mycursor = mydb.cursor()
sql = "DELETE FROM cliente WHERE IdCliente = '4'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "registro(s) deletado(s)")