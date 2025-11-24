#Aula de manipulação de strings
nome = "rIbERto"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "          Ola mundo!           "

print(texto)
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

menu = "Python"

print("####" + menu + "####")
print(menu.center(14)) # Faz a mesma coisa que o de cima de forma mais pratica

print(menu.center(14, "#"))

print("P-y-t-h-o-n")
print("-".join(menu)) # Faz a mesma coisa que o de cima de forma mais pratica

