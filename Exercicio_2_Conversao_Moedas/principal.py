from api.api import BuscaValorCorrente
from data.conexao import Banco_De_Dados

Data_Base = Banco_De_Dados()
err, conexao = Data_Base.conecta()

Pega_Ultima_Cotacao = Data_Base.Busca_Ultimo_Preco(conexao)
entrada = float(input("Informe um valor em R$ para ser convertido em Dólar e Euro: "))
if Pega_Ultima_Cotacao != None:
    print(f"Valor convertido para EURO: {entrada/float(Pega_Ultima_Cotacao[1])}")
    print(f"Valor convertido para Dólar: {entrada/float(Pega_Ultima_Cotacao[2])}")

else:
    print("Buscando dados e salvando no banco de dados...")
    err, Cotacao = BuscaValorCorrente(["USD","EUR"])
    Data_Base.Grava_Dados(conexao, Cotacao[0], Cotacao[1])
    print(f"Valor convertido para EURO: {entrada/float(Cotacao[1])}")
    print(f"Valor convertido para Dólar: {entrada/float(Cotacao[0])}")

conexao.close()