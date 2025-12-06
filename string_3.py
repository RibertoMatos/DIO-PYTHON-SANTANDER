#Fatiamento de strings

nome = "Pedro Alvares Cabral"

nome[0] # Primeira letra da string
print(nome[0])

nome[:9] # Do início até a posição 9 (sem incluir o caractere da posição 9)
print(nome[:9])

nome[10:]   # Da posição 10 até o final da string
print(nome[10:])

nome[11:13]     # Da posição 11 até a posição 13 (sem incluir o caractere da posição 13)   
print(nome[11:13])

nome[:] # Da posição 0 até o final da string
print(nome[:])

nome[:-1] # Da posição 0 até a penúltima posição
print(nome[::-1])

nome[:-1] # Utilizando indice negativo para mostrar a string invertida
print(nome[-1])
