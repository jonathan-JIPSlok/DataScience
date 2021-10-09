import re

texto = """Olá Mundo!
                   Meu nome é Jonathan Yuri.
                   Meu numero é (011) 988255673
                   Meu E-mail é Jonathanpoli17@Gmail.com
                   """
                   
Re_Padrao_Telefone = re.compile(r"\(\d{3}\)\s\d{9}") #Expreção que encontrara nosso numero
Resultado = Re_Padrao_Telefone.search(texto) #search Procura o numero no texto, findall procura todos os numeros disponiveis
print(Resultado.group()) #Group mostra oque foi encontrado, groups mostra mais de um
