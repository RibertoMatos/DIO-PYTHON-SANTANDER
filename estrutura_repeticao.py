texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#exemplo 1 - iterando sobre uma string
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print() # Apenas para pular uma linha após o loop


#exemplo 2 - utilizando o range
for numero in range(0, 51, 5): # start, stop, step
    print(numero, end=" ")