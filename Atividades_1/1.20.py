# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do 
# aumento e o novo salário.

salario = float(input("Informe o seu salário : "))
percentual_aumento = float(input("Informe o seu percentual de aumento. OBS trabalhamos com os valores de 0 à 100 : "))
novo_salario = (salario + (salario * percentual_aumento / 100))

print("O seu novo salário será de R${:.2f}".format(novo_salario))