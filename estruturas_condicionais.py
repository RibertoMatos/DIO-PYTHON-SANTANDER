MAIOR_IDADE = 18

idade = int(input("Iforme sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a cnh")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh")
else:
    print("Menor de idade, não pode tirar a cnh")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh")
elif idade == 17:
    print("Ainda não pode tirar a cnh, mas pode fazer as aulas teóricas")
else:
    print("Menor de idade, não pode tirar a cnh")



