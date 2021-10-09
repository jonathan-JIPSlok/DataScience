import json
from urllib.request import urlopen

dict = {"Nome":["Jonathan", "Claudete"], "Idade":["19", "42"]}
for key, value in dict.items():
    print(key, value)
    
    
def Convert_objectJson_write():
    with open("Arquivo.json", "w") as file:
        file.write(json.dumps(dict)) #json.dumps() converte o dicionario para um objeto json
    
    
def read_Json():
    with open("Arquivo_copia.json", "r") as file:
        text = file.read()
        data = json.loads(text) #grava um texto que esta escrito no arquivo
    print(data)
    

def json_internet():
    response = urlopen("URL.json").read().decode("utf8") #Lê o arquivo da internet decodificado em utf-8
    data = json.loads(response)[0]
    
    
def transferindo_conteudo():
    Infile = "Arquivo.json" #copiaremos
    Outfile = "Arquivo_copia.json" #colaremos
    
    with open(Infile, "r") as infile:
        text = infile.read()
        with open(Outfile, "w") as outfile:
            outfile.write(text)
            
            
def transferindo_conteudo_2metod():
    Infile = "Arquivo.json" #copiaremos
    Outfile = "Arquivo_copia.json" #colaremos
        
    open(Outfile, "w").write(open(Infile,"r").read())
    

