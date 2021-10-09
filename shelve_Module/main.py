import shelve

"""
    Permite salvar variaveis no disco rigido.
    Dessa maneira permitira adicionar o salvar em seu programa.
"""

ShelFile = shelve.open('MyData') #Cria/Abre um arquivo shelve
cats = ['Zophie', 'Dog', 'cat']
ShelFile['Cats'] = cats #É como um dicionario, você pode pegar e adicionar dados como se fosse um dict

print(ShelFile['Cats']) #Mostra os dados salvos em "Cats"

ShelFile.close() #Fecha a pasta