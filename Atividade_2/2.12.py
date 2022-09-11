# Faça um programa que receba:
# O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, isto é, um número inteiro entre 1 e 10.
# O peso do produto em quilos.
# O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um número inteiro entre 1 e 3.
print()
print("Código do País de Origem       Imposto")
print("1                              0%")
print("2                              15%")
print("3                              23%")
print()

codigo_pais = int(input("Informe o código referente ao País de origem: "))
while (codigo_pais < 1 or codigo_pais > 3 or codigo_pais % 2 != 0):
    codigo_pais = int(input("Informe apenas um número inteiro de acordo com o menu acima 1...3: "))

peso = float(input("Informe o peso do produto em kg: "))

print()
print("Código do Produto      Preço por Grama")
print("1 a 4                  10")
print("5 a 7                  25")
print("8 a 10                 35")
print()

codigo_produto = int(input("Informe o código referente ao País de origem: "))
while (codigo_produto < 1 or codigo_produto > 10 or codigo_produto % 2 != 0):
    codigo_produto = int(input("Informe apenas um número inteiro acordo com o menu acima 1...10: "))
