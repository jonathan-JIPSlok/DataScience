import sqlite3
import random
import datetime
import matplotlib.pyplot as plt
import numpy as np

Connection = sqlite3.connect("Data.db")
Cursor = Connection.cursor()

Cursor.execute("CREATE TABLE IF NOT EXISTS Dados(Data primary key, Valores interger)")

Valores = Cursor.execute("SELECT * FROM Dados").fetchall()
Data = []
valores = []

for linha in Valores:
    Data.append(linha[0])
    valores.append(linha[1])

Connection.commit()
Connection.close()

plt.bar(valores, Data) #plota um grafico em barras (eixo x, eixo  y)
plt.title("Grafico por Data") #Adiciona um titulo ao grafico
plt.show() #faz ela funciona