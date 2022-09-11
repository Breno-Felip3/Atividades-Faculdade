# Faça um programa que leia um número não determinado de pares de valores [m,n], todos inteiros e positivos, um par de cada vez, e que calcule e mostre a soma de todos os 
# números inteiros entre m e n (inclusive). A digitação de pares terminará quando m for maior ou igual a n.

numero = int(input("Informe um número inteiro e positivo: "))
somatoria = 0
while (True):
    if (numero % 2 != 0):
        print("Você digitou um número ímpar: ")
        numero = int(input("Informe um número inteiro e positivo: ")) 
        if not (numero < somatoria):
            break      
    while(numero % 2 == 0):
        somatoria += numero        
        print("A somatória dos números pares é = {}".format(somatoria))
        numero = int(input("Informe um número inteiro e positivo: "))
        
        
