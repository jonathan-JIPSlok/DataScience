import os

os.path.join('..', 'mongoDB') #Monta um diretorio com o separador correto do sistema

Diretory_Atual = os.getcwd() #Pega o diretorio Atual 

New_Diretory = os.chdir(os.path.join(Diretory_Atual, '..', 'mongoDB') ) #Muda o diretorio em que você está
