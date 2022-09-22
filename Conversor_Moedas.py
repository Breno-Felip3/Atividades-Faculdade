import requests

def conversor():
    link = "https://api.hgbrasil.com/finance?key=1428ecb9"
    a = requests.get(link)
    valor_USD = a.json()["results"]["currencies"]["USD"]["buy"]
    valor_EUR = a.json()["results"]["currencies"]["EUR"]["buy"]
    valor_Real = float(input("Informe o valor em Reais: "))
    convertido_valor_USD = valor_Real / valor_USD
    convertido_valor_EUR = valor_Real / valor_EUR
    return f"Valor convertido em Dólar = R${convertido_valor_USD:.2f}\n" \
        f"Valor convertido em Euro = R${convertido_valor_EUR:.2f}\n"

print(conversor())




