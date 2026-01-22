import sqlite3

#Pessoal para usar ess código baixem a extensão SQLITE VIEWER e executem esse arquivo, a tabela aparecerá
#no arquivo Acessol.db

connection = sqlite3.connect("Acessol.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE acessol_database (
               
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT NOT NULL,
               senha CHAR NOT NULL

                )""")

connection.commit()