# 1️⃣ Criar uma tupla com 5 dados
dados = ("maçã", "banana", "uva", "pera", "laranja")
print("Tupla original:", dados)

# 2️⃣ Transformar a tupla em uma lista
lista = list(dados)
print("Lista criada a partir da tupla:", lista)

# 3️⃣ Inserir 2 dados extras na lista
lista.append("melancia")
lista.append("abacaxi")
print("Lista com 2 itens adicionados:", lista)

# 4️⃣ Remover o primeiro dado da lista
lista.pop(0)  # remove o item na posição 0
print("Lista após remover o primeiro item:", lista)

# 5️⃣ Remover o último dado da lista
lista.pop()  # remove o último item
print("Lista após remover o último item:", lista)

# 6️⃣ Mostrar o primeiro dado da lista
print("O primeiro dado da lista é:", lista[0])

# 7️⃣ Mostrar a quantidade de dados da lista
print("A lista tem", len(lista), "itens.")

# 8️⃣ Criar um dicionário
pessoa = {
    "Nome": "Isla",
    "Idade": 26,
    "Profissão": "QA"
}

# 9️⃣ Imprimir somente o valor contido na chave 'Nome'
print("O nome da pessoa é:", pessoa["Nome"])
