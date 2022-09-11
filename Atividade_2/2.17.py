# Faça um programa para calcular a área de um triângulo e que não permita a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

base = float(input("Informe a medida da base do triângulo: "))
while (base <= 0):
    print("Você informou um valor inválido!")
    base = float(input("Vecê deve adicionar apenas números positivos: "))

altura = float(input("Informe a medida da altura do triângulo: "))
while (altura <= 0):
    print("Você informou um valor inválido!")
    altura = float(input("Vecê deve adicionar apenas números positivos: "))

area = (base * altura) / 2

print("A área do triângulo é = {}".format(area))
