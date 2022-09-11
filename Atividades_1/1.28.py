# Sabe-se que: pé = 12 polegadas; 1 jarda = 3 pés e 1 milha = 1,760 jarda. Faça um programa que receba uma medida em pés,
# faça as conversões a seguir e mostre os resultados.
# polegadas;
# jardas;
# milhas.

medida = int(input("Informe a media em pés: "))

polegadas = (medida * 12)
jardas = (medida / 3)
milhas = (jardas / 1760)



print("O valor convertido para polegadas é = {}".format(polegadas))
print("O valor convertido para jardas é = {}".format(jardas))
print("O valor convertido para milhas é = {}".format(milhas))