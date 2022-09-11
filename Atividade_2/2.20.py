# Faça um programa que receba vários números, calcule e mostre:
somatoria = 0
numero = float(input("Informe um número: "))
somatoria += numero
somatoria_pares = 0
total_numeros = 0
total_numeros_pares = 0
total_numeros_impares = 0
media = 0
percentual_impares = 0
maior_numero = numero
menor_numero = numero
while (numero != 0):
    numero = float(input("Informe um número: "))
    if (numero > maior_numero):
        maior_numero = numero
    if (numero < menor_numero and numero != 0):
        menor_numero = numero  
    if (numero % 2 == 0 and numero != 0):
        somatoria_pares += numero
        total_numeros_pares += 1
    elif(numero % 2 != 0 and numero != 0):
        total_numeros_impares += 1
    somatoria += numero
    total_numeros += 1


media = (somatoria / total_numeros)
media_pares = (somatoria_pares / total_numeros_pares)
percentual_impares =  (total_numeros_impares * 100) / total_numeros

print("A somatória de todos os número é {}".format(somatoria))
print("O total de número digitados foi de {} números".format(total_numeros))
print("A média dos números digitas é de {}".format(media))
print("O maior número digitado é o {}".format(maior_numero))
print("O menor número digitado é o {}".format(menor_numero))
print("A média dos número pares é {}".format(media_pares))
print("A porcentagem de números ímpares é de {}%".format(percentual_impares))
