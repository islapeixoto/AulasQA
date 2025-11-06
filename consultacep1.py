import requests

# Dicionário com os nomes e seus respectivos CEPs
integrantes = {
    "isla": "11635338",
    "marcelo": "11630391",
    "cecilia": "04013001"
}

# Percorre o dicionário de nomes e CEPs
for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()

        # Verifica se o CEP existe
        if "erro" in dados:
            print(f"O CEP de {nome} é inválido.")
        else:
            cidade = dados.get("localidade", "Cidade não encontrada")
            estado = dados.get("uf", "UF não encontrada")
            logradouro = dados.get("logradouro", "Sem logradouro")
            print(f"{nome.title()} mora em {cidade}/{estado}, na rua {logradouro}.")
    else:
        print(f"❌ Não foi possível localizar os dados de {nome}.")
