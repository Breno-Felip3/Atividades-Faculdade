# Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
# o número digitado ao quadrado;
# o número digitado ao cubo;
# a raiz quadrada do número digitado.

import math


numero = float(input("Informe um número positivo e maior que zero: "))
while(numero < 0):
    print("Você informou um número < 0, vamos tentar novamente? ")
    numero = float(input("Informe um número positivo e maior que zero: "))

quadrado = (numero ** 2)
cubo = (numero ** 3)
raiz = (math.sqrt(numero))

print("O quadrado do número é {}".format(quadrado))
print("O cubo do número é = {}".format(cubo))
print("A raiz do número é = {}".format(raiz))