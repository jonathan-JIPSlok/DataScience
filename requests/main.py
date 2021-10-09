import requests

res = requests.get("https://github.com/jonathan-JIPSlok/Aprendendo_Pandas") #faz o dowload de uma pagina web basta passar a URL

print(res.status_code == requests.codes.ok) #Verifica se foi baixado com sucesso

res.text # mostra o texto do arquivo

res.raise_for_status() #gera uma exeção se o dowload não tiver sido concluido, é uma maneira mais facil de verificar

#Gravando em um arquivo
playfile = open("Arquivo.html", "wb")
for chunk in res.iter_content(100000): #iter_content() permite gravar o arquivo
    playfile.write(chunk)
playfile.close()

"""
    O metodo iter_content() retorna "porções" do conteudo a cada interação pelo loop.
    Cada porção tem o tipo de dados bytes e é possivel especificar quantos bytes cada porção tera.
    Cem mil bytes geralmente é um bom tamanho.
"""