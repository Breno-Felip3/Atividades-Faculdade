# Faça um programa que receba o salário inicial de um funcionário, calcule e mostre o novo salário, acrescido de bonificação e de auxílio escola.

salario = float(input("Informe o valor do seu salário: "))

if (salario <= 500):
    bonificacao = (salario + (salario * 0.05) + 150)
    print("O seu novo salário é de R$ {:.2f}".format(bonificacao))

elif(salario <= 600):
    bonificacao = (salario + (salario * 0.12) + 150)
    print("O seu novo salário é de R$ {:.2f}".format(bonificacao))

elif(salario <= 1200):
    bonificacao = (salario + (salario * 0.12) + 100)
    print("O seu novo salário é de R$ {:.2f}".format(bonificacao))

else:
    bonificacao = (salario + 100)
    print("O seu novo salário é de {:.2f}".format(bonificacao))
