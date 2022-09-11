# Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.

a = float(input("Informe a primeira nota : "))
b = float(input("Informe a segunda nota : "))
c = float(input("Informe a terceira nota : "))

peso_a = float(1)
peso_b = float(1.7)
peso_c = float(2)

media_Ponderada = ((a * peso_a) + (b * peso_b) + (c * peso_c) / (peso_a + peso_b + peso_c))

print("A média ponderada de {}, {} e {} é = {:.2f}".format(a,b,c,media_Ponderada))