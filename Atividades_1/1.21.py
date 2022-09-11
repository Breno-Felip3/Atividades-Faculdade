#Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que 
# o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.

salario = int(input("Informe o seu salário base: "))

imposto = (salario - (salario * 0.07))

novo_salario = (imposto + (salario * 0.05))

print("O seu novo salário é = R$ {:.2f}".format(novo_salario))