# Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se 
# que o funcionário tem gratificação de R$ 50,00 e paga imposto de 10% sobre o salário base.

salario = int(input("Informe o seu salário base: "))

imposto = (salario - (salario * 0.10))

novo_salario = (imposto + 50)

print("O seu novo salário é = R$ {:.2f}".format(novo_salario))