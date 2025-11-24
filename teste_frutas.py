frutas = ["maçã", "banana", "laranja", "uva"]

while True:
	escolha = input("Qual fruta você quer? ").strip()
	if escolha in frutas:
		print(f"Temos {escolha}!")
		break
	else:
		print("Não tenho essa fruta. Tente novamente.")