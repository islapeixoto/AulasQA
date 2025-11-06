
nome_pet = input("Digite o nome do pet: ")
idade_humana = int(input("Digite a idade humana do pet (em anos): "))
porte = input("Digite o porte do pet (pequeno, medio ou grande): ").lower()
banhos = int(input("Quantos banhos ele tomou nos últimos 12 meses? "))


idade_cachorro = idade_humana * 7


if porte == "pequeno":
    lucro_por_banho = 50 - 5
elif porte == "medio":
    lucro_por_banho = 60 - 15
elif porte == "grande":
    lucro_por_banho = 75 - 20
else:
    print("Porte inválido! Digite pequeno, medio ou grande.")
    lucro_por_banho = 0


lucro_total = lucro_por_banho * banhos


print(f"\nOlá, {nome_pet} tem {idade_cachorro} anos em idade canina 🐾")
print(f"Nos últimos 12 meses, o lucro com este animal foi de R${lucro_total:.2f}")
