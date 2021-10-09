seq1 = [1, 2, 3, 4]
seq2 = [4, 3, 2, 1]

print(list(zip(seq1, seq2))) # zip agrega os falores de 2 sequencias

print(list(enumerate(seq1))) # enumerate retorna o indice de cada valor de uma sequencia, (indice, valor)