import mysql.connector


connection = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     password = 'x',
     database = 'labo_sys'
)

cursor = connection.cursor()




