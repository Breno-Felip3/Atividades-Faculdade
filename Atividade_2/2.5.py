import math

print()
print("Menu de opcões:")
print("1. Somar dois números")
print("2. Raiz quadrada de um número")
print()
escolha = int(input("Informe a operação desejada: "))

while (escolha != 1 and escolha != 2):
    escolha = int(input("Você deve escolher apenas os números correspondentes ao menu de opções: "))

if (escolha == 1):
    print("Você escolheu somatória de dois números!")
    numero_1 = int(input("Informe o primeiro número: "))
    numero_2 = int(input("Informe o segundo número: "))
    somataria = (numero_1 + numero_2)
    print("A soma de {} + {} é = {}".format(numero_1, numero_2,somataria))

else:
    print("Você escolheu Raiz quadrada de um número:")
    numero = float(input("Informe o número para extrair a sua raiz: "))
    raiz = math.sqrt(numero)
    print("A raiz de {} é = {:.2f}".format(numero, raiz))