# Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se 
# que este sofreu um aumento de 25%.

salario = float(input("Informe o seu salário : "))
novo_salario = (salario + (salario * 0.25))

print("O seu novo salário será de R${:.2f}".format(novo_salario))