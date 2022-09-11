# Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento 
# e o valor total depois do rendimento.


deposito = float(input("Informe o valor do depósito: "))
juros = float(input("Informe o percentual de juros, sendo de 0.0 à 1 = 100%: "))

rendimento = (deposito * juros)
valor_total = (deposito + rendimento)

print("O valor do rendimento é de R$ {:.2f}".format(rendimento))
print("O valor total é de R$ {:.2f}".format(valor_total))

