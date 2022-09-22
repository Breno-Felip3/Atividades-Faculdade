import requests

def busca_endereco():
    print("Escolha a opção que deseja buscar o endereço: \n"
          "[1] CEP \n"
          "[2] Nome da Rua")
    escolha = int(input("Informe a opção escolhida: "))

    if escolha == 1:
        cep = (input("Digire o cep: "))
        url = f"https://viacep.com.br/ws/{cep}/json/"
        dados = requests.get(url)
        nome_rua = dados.json()["logradouro"]
        nome_bairro = dados.json()["bairro"]
        nome_cidade = dados.json()["localidade"]
        nome_estado = dados.json()["uf"]
        cep_formatado = dados.json()["cep"]
        return f"{nome_rua} - {nome_bairro}, {nome_cidade} - {nome_estado}, {cep_formatado}"
    elif escolha == 2:
        estado = input("Informe o seu estado: ")
        cidade = input("Informe a cidade: ")
        rua = input("Informe o nome da rua: ")
        url = f"https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json/"
        dados = requests.get(url)
        nome_bairro = dados.json()[0]["bairro"]
        cep_formatado = dados.json()[0]["cep"]
        return f"{rua} - {nome_bairro}, {cidade} - {estado}, {cep_formatado}"
    else:
        return 'Opção inválida'

print(busca_endereco())