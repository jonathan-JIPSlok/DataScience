import zipfile
import os

Zip = zipfile.ZipFile("OLAMUNDO.zip") #Abre um arquivo zip

print(Zip.namelist()) #retorna todos os arquivos contidos

Zipinfo = Zip.getinfo('OLAMUNDO/newfile.py') #retorna um objeto getinfo associado a este arquivo
print(Zipinfo.file_size) #Mosta o tramanho do arquivo em bites
print(Zipinfo.compress_size) #Mostra o tamanho do arquivo compactado em bites

#Zip.extractall() #Extrai todos os arquivos e as pastas de um aqruovo ZIP no diretorio atual, pode receber um parametro que sera o local de extracao
#Zip.extract("OLAMUNDO/newfile.py", os.getcwd()) #Extrai um unico arquivo do arquivo zip

zip = zipfile.ZipFile('new.zip', 'w') #Cria um novo arquivo zip em modo de escrita
#quandor for apenas adicionar conteudo abra o arquivo em "a" modo append
zip.write('OLAMUNDO', compress_type = zipfile.ZIP_DEFLATED) #Escreve no arquivo
#1 argumento é a pasta que sera conpactada
#2 argumento é o tipo de compactação