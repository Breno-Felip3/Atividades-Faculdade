# Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.

numero_1 = float(input("Informe o primeiro número positivo e maior que zero: "))
while(numero_1 < 0):
    print("Você informou o primeiro número < 0, vamos tentar novamente? ")
    numero_1 = float(input("Informe um número positivo e maior que zero: "))

numero_2 = float(input("Informe o segundo número positivo e maior que zero: "))
while(numero_2 < 0):
    print("Você informou um número < 0, vamos tentar novamente? ")
    numero_2 = float(input("Informe o segundo número positivo e maior que zero: "))

potencia = (numero_1 ** numero_2)

print("O número {} elevado ao número {} é = {}".format(numero_1, numero_2, potencia))