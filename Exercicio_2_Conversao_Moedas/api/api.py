import requests, json

def BuscaValorCorrente(types):
    try:
        requisicao = requests.get("https://api.hgbrasil.com/finance?key=1428ecb9")
        if requisicao.status_code == 200:
            objeto = json.loads(requisicao.text)
            dados = []
            for i in range(len(types)):
                dados.append(objeto["results"]["currencies"][types[i]]["buy"])
                pass
            return False, dados
        else:
            return True, "Sistema indisponível"
    except Exception as e:
        return True, e