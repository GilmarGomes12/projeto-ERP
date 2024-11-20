import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1305",
        database="erp"
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro: {err}")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cliente")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)