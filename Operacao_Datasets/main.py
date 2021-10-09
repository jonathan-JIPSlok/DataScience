import csv

def open_to_read():
    """
        Abrindo o arquivo csv para leitura
    """
    file = open("Arquivo_csv.csv", "r") # "r" é o modo de leitura
    data = file.read() # read() serve para ler todo o arquivo
    rows = data.split("\n") #split() separa as linhas por "/n"
    print(rows)
    
def dividindo_dataset_porcolumn(): #Divide o dataset por coluna
    file = open("Arquivo_csv.csv", "r")
    data = file.read()
    rows = data.split("\n")
    full_data = []
    for row in rows: # percorre linha por linha
        split_row = row.split(",") #separa as colunas por ","
        full_data.append(split_row) # adiciona as linhas a lista que tera todas as linhas
    
    print(full_data)
    
def rows_count():
    file = open("Arquivo_csv.csv", "r")
    data = file.read()
    rows = data.split("\n")
    full_data = []
    for row in rows:
        split_row = row.split(",")
        full_data.append(split_row)
    count = -1
    for row in full_data:
        count += 1
    print("Linhas: ", count)
    
def column_count():
    file = open("Arquivo_csv.csv", "r")
    data = file.read()
    rows = data.split("\n")
    full_data = []
    for row in rows:
        split_row = row.split(",")
        full_data.append(split_row)
        frist_row = full_data[0]
    count = 0
    for column in frist_row:
        count += 1
    print("Colunas: ", count)
    
open_to_read()
print()

dividindo_dataset_porcolumn()
print()

rows_count()
print()

column_count()