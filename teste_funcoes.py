#modelo basico de funcao sem parametros e sem retorno
def cabecario():
    print("Seja bem vindo ao sistema de cadastro!")
    

def rodape():
    print ("Obrigado por utilizar nosso sistema!")

cabecario()

print()

rodape()

#modelo basico de funcao com parametros e sem retorno
def salvar_carros(marca, modelo, ano, placa):
    print(f"Carro salvo: {marca} {modelo} {ano} {placa}")

# Chamadas da funcao salvar_carros
salvar_carros("Volkswagen","Fox","2008","ABC-9I23")

# Chamadas da funcao salvar_carros com argumentos nomeados
salvar_carros(marca="Volkswagen",modelo="Fox",ano="2008",placa="ABC-9I23")

# Chamadas da funcao salvar_carros com dicionario e desempacotamento
#salvar_carros(**{"marca":"Volkswagen","modelo":"Fox","ano":"2008","placa":"ABC-9I23"})
salvar_carros()