# Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. 
# Os cargos estão na tabela a seguir.
aumento = 0
novo_salario = 0
print()
print("Código       Cargo       Percentual")
print("1         Escrituário       50%")
print("2         Secretário        35%")
print("3         Caixa             20%")
print("4         Gerente           10%")
print("5         Diretor           0%")
print()

codigo = int(input("Informe o código referente ao seu cargo: "))
while (codigo < 1 or codigo > 5):
    codigo = int(input("Informe apenas códigos de acordo com o menu acima 1...5: "))

salario = float(input("informe o seu salário atual: "))

if (codigo == 1):
    aumento = (salario * 0.5)
    novo_salario = (salario + aumento)
    print("O seu cargo é Escrituário")
    print("O valor de aumento é de R$ {:.2f}".format(aumento))
    print("O seu novo salário é de R$ {:.2f}".format(novo_salario))

elif (codigo == 2):
    aumento = (salario * 0.35)
    novo_salario = (salario + aumento)
    print("O seu cargo é Secretário")
    print("O valor de aumento é de R$ {:.2f}".format(aumento))
    print("O seu novo salário é de R$ {:.2f}".format(novo_salario))

elif (codigo == 3):
    aumento = (salario * 0.20)
    novo_salario = (salario + aumento)
    print("O seu cargo é Caixa")
    print("O valor de aumento é de R$ {:.2f}".format(aumento))
    print("O seu novo salário é de R$ {:.2f}".format(novo_salario))

elif (codigo == 4):
    aumento = (salario * 0.10)
    novo_salario = (salario + aumento)
    print("O seu cargo é Gerente")
    print("O valor de aumento é de R$ {:.2f}".format(aumento))
    print("O seu novo salário é de R$ {:.2f}".format(novo_salario))

else:
    print("O seu cargo é Diretor")
    print("Você não está habilitado para ter aumento salarial! ")
 

