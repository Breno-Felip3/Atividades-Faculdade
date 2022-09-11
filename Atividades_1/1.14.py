# Faça um programa que leia dois números inteiros e imprima o dividendo, divisor, quociente e resto da divisão

a = int(input("Informe o primeiro número inteiro: "))
b = int(input("Informe o segundo número inteiro: "))

divisao = (a / b)
resto = (a % b)

print("O dividendo é o {}".format(a))
print("O divisor é o {}".format(b))

print("O quociente é o {}".format(divisao))
print("O resto da divisão é o {}".format(resto))

