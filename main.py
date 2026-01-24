import sqlite3

#Pessoal para usar ess código baixem a extensão SQLITE VIEWER e executem esse arquivo, a tabela aparecerá
#no arquivo Acessol.db

connection = sqlite3.connect("Acessol.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE acessol_usuario (
               
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT NOT NULL,
               senha CHAR NOT NULL

                )""")

cursor.execute("""CREATE TABLE acessol_adm (

                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha CHAR NOT NULL
  
                ) """)

cursor.execute("""CREATE TABLE acessol_empresas (
                
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                cnpj INTEGER NOT NULL,
                



                ) """)

cursor.execute("DROP TABLE acessol_usuario;")

connection.commit()