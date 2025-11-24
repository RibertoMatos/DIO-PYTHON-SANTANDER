#Interpolação e formatação de variaveis em Python
nome = "Riberto"
idade = 40
profissao = "Analista"
linguagem = "Python"
altura = 1.750
dados = {"nome":"Riberto", "idade": 40, "profissao": "Analista", "linguagem": "Python"}


# Exemplo de formatação de strings usando o operador %
print("Nome: %s Idade: %d Profissão: %s Linguagem: %s" % (nome, idade, profissao, linguagem))

# Exemplo de formatação de strings usando o método format()
print("Nome: {} Idade: {} Profissão: {} Linguagem: {}".format(nome, idade, profissao, linguagem))
# Exemplo de formatação de strings usando o método format() com índices
print("Nome: {1} Idade: {3} Profissão: {2} Linguagem: {0}".format(linguagem, nome, profissao, idade))
# Exemplo de formatação de strings usando f-strings (Python 3.6+)
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}")
# Exemplo de formatação de strings usando dicionários com o método format()
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**dados))
# Exemplo de formatação de strings usando dicionários com f-strings (Python 3.8+)
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}")
# Exemplo de formatação de strings com f-strings e formatação numérica
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Altura: {altura:.2f}m")