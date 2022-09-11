# Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir.

nota_1 = float(input("Informa o valor da primeira nota, de 0 a 10: "))
nota_2 = float(input("Informa o valor da primeira nota, de 0 a 10: "))
nota_3 = float(input("Informa o valor da primeira nota, de 0 a 10: "))

nota = (nota_1  + nota_2  + nota_3 ) / 3
print()
if (nota >= 7):
    print("Aprovado")
elif (nota >= 3 and nota < 7):
    print("Exame Especial")
else:
    print("Reprovado")