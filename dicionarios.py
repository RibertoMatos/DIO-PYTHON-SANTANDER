# Dicionários aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print (contatos["giovanna@gmail.com"]["telefone"])

telefone = contatos["chappie@gmail.com"]["telefone"]
print(telefone)

dados = contatos["melaine@gmail.com"]

print(dados)

# Iterar dicionarios com for

for chave in contatos:
    print(chave, contatos[chave])

# iterar dicionarios com items()

for chave, valor in contatos.items():
    print(chave, valor)