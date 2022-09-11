# A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de 
# laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:
# Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela:

nota_trabalho = float(input("Informa o valor da primeira nota, de 0 a 10: "))
nota_avaliacao = float(input("Informa o valor da primeira nota, de 0 a 10: "))
nota_exame = float(input("Informa o valor da primeira nota, de 0 a 10: "))

nota = ((nota_trabalho * 2) + (nota_avaliacao * 3 ) + (nota_exame * 5)) / 10

if (nota >= 8):
    print("Conceito A")
elif (nota >= 7 and nota <= 8):
    print("Conceito B")
elif (nota >= 6 and nota <= 7):
    print("Conceito C")
elif (nota >= 5 and nota <= 6):
    print("Conceito C")
else:
    print("Conceito C")