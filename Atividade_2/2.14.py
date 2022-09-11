# Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:
# Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
# Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
# A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.

salario_inicial = 1015
percentual_aumento = 0.015

for x in range(1,17):
    percentual_aumento = (percentual_aumento * 2)
    
salario_atual = ((salario_inicial + salario_inicial * percentual_aumento) / 100)

print("O salário atual deste funcionário é de R$ {:.2f}".format(salario_atual))
