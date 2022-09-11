#Calculando o IMC

from tokenize import Double


altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = (peso / (altura * altura))

print ("O seu IMC é = {:.2f}".format(imc))