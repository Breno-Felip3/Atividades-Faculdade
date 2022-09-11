# Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verifique se é um triângulo equilátero, isósceles ou escaleno. 
# Se eles não formarem um triângulo, escreva uma mensagem. Considere que:

x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))
z = float(input("Informe o valor de z: "))

if ((x < (y + z)) and (y < (x + z)) and (z < (x + z))):
    if (x == y and x == z):
        print("Esse é um triâgulo equilátero!")
    elif (x == z or x == y or y == z):
        print("Esse é um triângulo isósceles! ")
    else:
        print("Esse é um triângulo escaleno! ")
else:
    print("Esses valores não formam um triângulo! ")