# Exemplo de uso do método clear() em dicionários
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.clear()
contatos

# Exemplo de uso do método copy() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
contatos["guilherme@gmail.com"] 
copia["guilherme@gmail.com"] 

# Exemplo de uso do método {}.fromkeys em dicionários

dict.fromkeys(["nome", "telefone"]) 
dict.fromkeys(["nome", "telefone"], "vazio")

# Exemplo de uso do método get() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
contatos["chave"] # KeyError
contatos.get("chave") # None
contatos.get("chave", {}) # {} retorna vazio
contatos.get("guilherme@gmail.com", {})

# Exemplo de uso do método items() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.items() 

# Exemplo de uso do método keys() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.keys() 

# Exemplo de uso do método pop() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone': '3333-
2221'}
contatos.pop("guilherme@gmail.com", {})

# Exemplo de uso do método popitem() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.popitem()
contatos.popitem() # KeyError

# Exemplo de uso do método setdefault() em dicionários

contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("nome", "Giovanna") # "Guilherme"
contato # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("idade", 28) # 28
contato # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

# Exemplo de uso do método update() em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}}
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos

# Exemplo de uso do método values() em dicionários, retornoa os valores sem a chave

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.values() 

# Exemplo de uso do método in em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False
"idade" in contatos["guilherme@gmail.com"] # False
"telefone" in contatos["giovanna@gmail.com"] # True

# Exemplo de uso do método del em dicionários

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]
contatos