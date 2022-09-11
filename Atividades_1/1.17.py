# Faça um programa que receba três notas, calcule e mostre a média aritmética.

a = float(input("Informe a primeira nota : "))
b = float(input("Informe a segunda nota : "))
c = float(input("Informe a terceira nota : "))

media = ((a + b + c) / 3)

print("A média de {}, {}, e {} é {:.2f}".format(a, b, c, media))