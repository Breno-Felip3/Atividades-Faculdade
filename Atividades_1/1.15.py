# Escreva um programa que solicite do usuário dois números, e imprima o resultado da soma, 
# subtração, multiplicação e divisão.

a = float(input("Informe o primeiro número : "))
b = float(input("Informe o segundo número : "))

somatoria = (a + b)
subtracao = (a - b)
multiplicacao = (a * b)
divisao = (a / b)

print("A somatória de {} + {} é = {}".format(a,b,somatoria))
print("A subtração de {} - {} é = {}".format(a,b,subtracao))
print("A multiplicação de {} * {} é = {}".format(a,b,multiplicacao))
print("A divisão de {} / {} é = {}".format(a,b,divisao))
