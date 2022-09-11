#  Faça um programa que receba duas notas de seis alunos. Calcule e mostre
total_alunos_aprovados = 0
total_alunos_exame = 0
total_alunos_reprovados = 0
media_classe = 0

Aluno_1_nota_1 = float(input("Informe a primeira nota do Aluno 01: "))
Aluno_1_nota_2 = float(input("Informe a segunda nota do Aluno 01: "))
media_aluno_1 = (Aluno_1_nota_1 + Aluno_1_nota_2) / 2
print("A média aritmética do Aluno 01 é = {}".format(media_aluno_1))
if (media_aluno_1 <= 29):
    print("Aluno reprovado")
    total_alunos_reprovados += 1
elif(media_aluno_1 <= 69):
    print("O aluno deve fazer o Exame Especial")
    total_alunos_exame += 1
else:
    print("Aluno Aprovado")
    total_alunos_aprovados += 1   
print()
Aluno_2_nota_1 = float(input("Informe a primeira nota do Aluno 02: "))
Aluno_2_nota_2 = float(input("Informe a segunda nota do Aluno 02: "))
media_aluno_2 = (Aluno_2_nota_1 + Aluno_2_nota_2) / 2
print("A média aritmética do Aluno 02 é = {}".format(media_aluno_2))
if (media_aluno_2 <= 29):
    print("Aluno reprovado")
    total_alunos_reprovados += 1
elif(media_aluno_2 <= 69):
    print("O aluno deve fazer o Exame Especial")
    total_alunos_exame += 1
else:
    print("Aluno Aprovado")
    total_alunos_aprovados += 1
print()
Aluno_3_nota_1 = float(input("Informe a primeira nota do Aluno 03: "))
Aluno_3_nota_2 = float(input("Informe a segunda nota do Aluno 03: "))
media_aluno_3 = (Aluno_3_nota_1 + Aluno_3_nota_2) / 2
print("A média aritmética do Aluno 03 é = {}".format(media_aluno_3))
if (media_aluno_3 <= 29):
    print("Aluno reprovado")
    total_alunos_reprovados += 1
elif(media_aluno_3 <= 69):
    print("O aluno deve fazer o Exame Especial")
    total_alunos_exame += 1
else:
    print("Aluno Aprovado")
    total_alunos_aprovados += 1
print()
Aluno_4_nota_1 = float(input("Informe a primeira nota do Aluno 04: "))
Aluno_4_nota_2 = float(input("Informe a segunda nota do Aluno 04: "))
media_aluno_4 = (Aluno_4_nota_1 + Aluno_4_nota_2) / 2
print("A média aritmética do Aluno 04 é = {}".format(media_aluno_4))
if (media_aluno_4 <= 29):
    print("Aluno reprovado")
    total_alunos_reprovados += 1
elif(media_aluno_4 <= 69):
    print("O aluno deve fazer o Exame Especial")
    total_alunos_exame += 1
else:
    print("Aluno Aprovado")
    total_alunos_aprovados += 1
print()
Aluno_5_nota_1 = float(input("Informe a primeira nota do Aluno 05: "))
Aluno_5_nota_2 = float(input("Informe a segunda nota do Aluno 05: "))
media_aluno_5 = (Aluno_5_nota_1 + Aluno_5_nota_2) / 2
print("A média aritmética do Aluno 05 é = {}".format(media_aluno_5))
if (media_aluno_5 <= 29):
    print("Aluno reprovado")
    total_alunos_reprovados += 1
elif(media_aluno_5 <= 69):
    print("O aluno deve fazer o Exame Especial")
    total_alunos_exame += 1
else:
    print("Aluno Aprovado")
    total_alunos_aprovados += 1
print()
Aluno_6_nota_1 = float(input("Informe a primeira nota do Aluno 06: "))
Aluno_6_nota_2 = float(input("Informe a segunda nota do Aluno 06: "))
media_aluno_6 = (Aluno_6_nota_1 + Aluno_6_nota_2) / 2
print("A média aritmética do Aluno 06 é = {}".format(media_aluno_6))
if (media_aluno_6 <= 29):
    print("Aluno reprovado")
    total_alunos_reprovados += 1
elif(media_aluno_6 <= 69):
    print("O aluno deve fazer o Exame Especial")
    total_alunos_exame += 1
else:
    print("Aluno Aprovado")
    total_alunos_aprovados += 1
print()
media_classe = (media_aluno_1 + media_aluno_2 + media_aluno_3 + media_aluno_4 + media_aluno_5 + media_aluno_6) / 6
print()
print("O total de alunos aprovados foi {}".format(total_alunos_aprovados))
print("O total de alunos que deve fazer o exame especial é {}".format(total_alunos_exame))
print("O total de alunos reprovados é {}".format(total_alunos_reprovados))
print("A média geral da classe é {}".format(media_classe))