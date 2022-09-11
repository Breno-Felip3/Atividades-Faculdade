# Faça um programa que receba um número inteiro e verifique se é par ou ímpa

numero = int(input("Informe um número inteiro: "))

if(numero % 2 == 0):
    print("O número {} é Par!".format(numero))
else:
    print("O número {} é ímpar!".format(numero))
    
