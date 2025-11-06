
valor = float(input("Digite um número: "))


dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor ** 0.5     # mesma coisa que sqrt(valor)
raiz_cubica = valor ** (1/3)


print(f"\nO dobro de {valor} é {dobro}")
print(f"O triplo de {valor} é {triplo}")
print(f"O valor de {valor} ao quadrado é {quadrado}")
print(f"A raiz quadrada de {valor} é {raiz_quadrada:.2f}")
print(f"A raiz cúbica de {valor} é {raiz_cubica:.2f}")
