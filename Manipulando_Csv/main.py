import csv

with open("Arquivo.csv", "w") as file: # mantem o arquivo aberto enquanto é usado
    writer = csv.writer(file) # Prepara para escrever no arquivo
    writer.writerow(("Nome", "Idade", "Sexo")) #Escreve no arquivo
    writer.writerow(("Jonathan", "19", "Masculino"))
    writer.writerow(("Claudete", "42", "Feminino"))
    
print()
with open("Arquivo.csv", "r") as file:
    reader = csv.reader(file) #lê o arquivo
    for x in reader:
        print("Numero de colunas: ", len(x))
        print(x)
        
print()
with open("Arquivo.csv", "r") as file:
    reader = csv.reader(file)
    datas = list(reader) #Coloca os dados em uma lista
    print(datas)
    print()
    
    for row in datas[1:]: # pega linha por linha a partir da linha 1
        print(row)