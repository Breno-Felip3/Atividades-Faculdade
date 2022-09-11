# Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço aumentado ou diminuído. Para o preço ser alterado, 
# o produto deve preencher pelo menos um dos requisitos a seguir:

venda_mensal = int(input("Informe qual é a venda média mensal: "))
preco_atual = float(input("Informe qual é o preço atual do produto: "))

if (venda_mensal < 500 & preco_atual < 30):
    novo_preco = (preco_atual + (preco_atual * 0.1))
    preco_atual("O novo preço do produto é de R$ {:.2f}".format(novo_preco))

elif (venda_mensal < 1200 & preco_atual >= 30 & preco_atual < 80):
    novo_preco = (preco_atual + (preco_atual * 0.15))
    preco_atual("O novo preço do produto é de R$ {:.2f}".format(novo_preco))

else:
    novo_preco = (preco_atual - (preco_atual * 0.2))
    preco_atual("O novo preço do produto é de R$ {:.2f}".format(novo_preco))
