import sqlite3

con = sqlite3.connect("Data.db") #Cria o banco de dados
cur = con.cursor() #Permite fazer coisas dentro do banco de dados

cur.execute("CREATE TABLE IF NOT EXISTS Cursos(ID interger primary key, Nome varchar(100), Valor interger)")
#execute Permite executar coisas dentro do banco de dados
#CREATE TABLE IF NOT EXISTS cria uma tabela no bd caso ela ainda não exista

#cur.execute("INSERT INTO Cursos(ID, Nome, Valor) VALUES(?, ?, ?)", (1093822, "Inglês", "889.50"))
#INSERT serve para inserir valores dentro do banco de dados
con.commit() #salva as alteracoes feitas no banco de dados

lista = cur.execute("SELECT * FROM Cursos") #Pega um objeto com todos os items do banco de dados
print(lista.fetchall()) #pega os dados de dentro do objeto sqlite3

cur.execute("UPDATE Cursos SET Valor = 989.50 WHERE Valor = 889.50")
con.commit()
#UPDATE muda dados da tabela do banco de dados

lista = cur.execute("SELECT * FROM Cursos") #Pega um objeto com todos os items do banco de dados
print(lista.fetchall()) #pega os dados de dentro do objeto sqlite3

con.close()