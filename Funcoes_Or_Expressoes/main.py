def add_one(valor):
    return valor + 1
    
valores = [20, 11, 34, 45]

print(list(map(add_one, valores))) # map recebe uma funcao e uma sequencia e aplica esta funcao a cada item da sequencia
print()

print(list(map(lambda x: (5.0/9)*(x - 32), valores))) #transformando os dados como se fossem graus em fahrenheit
print()

def impar(valor):
    if valor % 2 == 0:
        return False
    else: return True
   
print(list(filter(impar, valores))) #filter aceita apenas funcoes que retornam True e False, ele manda cada item da lista para a funcao e só pega de volta aqueles que a funcao retornou como True
print()

