# Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor 
# negativo ou zero.

import math
somatória = 0
total_numeros = 0
numero = float(input("Informe um número: "))
somatória += numero
while(numero > 0):
    numero = float(input("Informe um número: "))
    somatória += numero
    total_numeros += 1
print()
quadrado = (somatória * somatória)
cubo = (somatória ** 3)
raiz = math.sqrt(somatória)

print("A somatória dos números lidos é de {}".format(somatória))
print("A quantidade de números informados é de {}".format(total_numeros))
print("O quadrado do número {} é = {}".format(somatória, quadrado))
print("O cubo do número {} é = {}".format(somatória, cubo))
print("A raiz do número {} é = {:.2f}".format(somatória, raiz))


