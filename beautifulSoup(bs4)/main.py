import bs4, requests

#É um modulo usado para extrair informacoes de uma pagina web

#bs4.BeautifulSoup() #Deve ser chamado com uma string contendo o html em que o parse sera feito.

res = requests.get("https://jonathan-jipslok.github.io/")
res.raise_for_status()

Jip = bs4.BeautifulSoup(res.text)
Jip.select('div') #Pega elementos e tags
Jip.select('#produto') #pega elementos por id
Jip.select('.Produtos') #Pega elementos class
Jip.select('div span') #pega elementos <span> que estejam dentro de uma div
Jip.select('div > span') #Pega elementos <span> que estejam direyamente em um elemento chamado <div>, sem que haja outros elementos intermediarios
Jip.select('input[name]') #pega elementos <input> que tenham atributo name
Jip.select('input[type = "buttom"]') #pega elementos <input> que tenha atributo type de valor buttom

Jip.attrs# {id:autor}

#DOWLOAD DE IMAGENS
res = requests.get("https://animesonline.org/episodio/boruto-naruto-next-generations-episodio-32/")
soup = bs4.BeautifulSoup(res.text)
comicElement = soup.select('img')
print(comicElement)
if comicElement == []:
    print('sem imagens')
else:
    print()
    comicUrl = comicElement[0].get('src')
    print(f"dowload img {comicUrl}")
    
    
    res = requests.get(comicUrl)
    res.raise_for_status()
    with open('img.png', 'w') as img:
        img.write(res.text)
    print("done")
    