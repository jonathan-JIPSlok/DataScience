
list = [x for x in "Python"] #Cria uma lista com cada letra da palavra

list = [x**5 for x in range(0, 20)] #Multiplica cada numero do range por 5 e torna uma lista com os valores

list = [x for x in range(11) if x % 2 == 0] #Cria uma lista com cada numero do range que o resto da divisao por 2 seja 0 ou seja cada numero par

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((float(9)/5) * temp + 32) for temp in celsius] #transforma graus celsius em fahrenheit
print(fahrenheit)

list = [x**2 for x in [x**2 for x in range(5)]] #uma list comprehension dentro de outra

print(list)