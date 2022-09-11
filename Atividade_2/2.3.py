# Faça um programa que receba dois números e mostre o maior.

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))

if (a > b):
    print("{} é maior que {}".format(a,b))
elif (a < b):
    print("{} é maior que {}".format(b,a))
else:
    print("{} é = {}".format(a,b))

