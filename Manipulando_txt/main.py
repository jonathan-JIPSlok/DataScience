import os

Texto = """Ola Amigos!\nHoje vim aqui contar a vocês que...\nNós somos muito bons naquilo que fazemos e é por isso que não podemos deixar ninguem dizer o contrario.\n
"""

file = open(os.path.join("Arquivo.txt"), "w") #abre o arquivo

for palavra in Texto: #pega cada palavra do texto
    file.write(palavra) #escreve as palavras no arquivo
    
file.close

file = open("Arquivo.txt", "r")
conteudo = file.read() #le o arquivo
print(conteudo)