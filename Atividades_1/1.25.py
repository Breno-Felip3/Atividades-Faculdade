# Escreva um programa que receba como entrada o raio de um círculo e imprima o diâmetro, a circunferência e a área. 
# Para isso, utilize as fórmulas: diâmetro = 2r; circunferência = 2πr, área = πr².

raio = float(input("Informe qual é o valor do raio do triângulo: "))

diametro = (raio * 2)
circunferencia = (2 * 3.14 * raio)
area = (3.14 * (raio * raio))

print("O diâmetro do círculo é = {}".format(diametro))
print("A circunferência do círculo é = {}".format(circunferencia))
print("A área do círculo é = {}".format(area))
