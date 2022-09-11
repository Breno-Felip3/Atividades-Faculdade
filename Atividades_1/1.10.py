# Faça um programa que leia um número inteiro e imprima seu número sucessor e antecessor.

numero = int(input("Informe um número inteiro: "))

sucessor = (numero + 1)
antecessor = (numero - 1)

print("O número posterior à {} é {}".format(numero,sucessor))
print("O número anterior à {} é {}".format(numero,antecessor))