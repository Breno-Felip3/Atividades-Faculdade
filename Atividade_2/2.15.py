# Foi feita uma pesquisa para determinar o índice de mortalidade infantil em certo período. Faça um programa que:

numero_M = int(input("Informe a quantidade de crianças do sexo Masculino nascidas entre janeiro de 2020 e Agosto de 2022: "))
numero_F = int(input("Informe a quantidade de crianças do sexo Feminino nascidas entre janeiro de 2020 e Agosto de 2022: "))

mortalidade_F = int(input("Informe a quantidade de crianças do sexo Feminino falecidas entre janeiro de 2020 e Agosto de 2022: "))
mortalidade_M = int(input("Informe a quantidade de crianças do sexo Masculino falecidas entre janeiro de 2020 e Agosto de 2022: "))


percentual_F = ((mortalidade_F / numero_F) * 100)
print("A porcentagem de crianças do sexo feminino mortas no período é de {}%".format(percentual_F))
percentual_M = ((mortalidade_M / numero_M) * 100)
print("A porcentagem de crianças do sexo masculino mortas no período é de {}%".format(percentual_M))

numero_Total = (numero_M + numero_F)
mortalidade_Total = (mortalidade_F + mortalidade_M)
criancas_sobreviventes = (numero_Total - mortalidade_Total)

percentual_Total = ((criancas_sobreviventes * 100) / numero_Total)
print("A porcentagem de crianças sobreviventes no período é de {}%".format(percentual_Total))