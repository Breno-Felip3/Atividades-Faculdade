import sqlite3
import uuid
from datetime import datetime


class Banco_De_Dados:
    def conecta(self):
        try:
            conexao = sqlite3.connect("data/cotacoes.db")
            return False, conexao
        except Exception as e: 
            return True, e

    def Busca_Ultimo_Preco(self, conexao):
        comando = conexao.cursor()
        executa_comando_SQL = comando.execute("Select * from Cotacoes where Data = '"+str(datetime.today().strftime('%Y-%m-%d'))+"'")
        dados = executa_comando_SQL.fetchone()
        return dados
    
    def Grava_Dados(self, conexao, cotacao_USD, cotacao_EUR):
        comando = conexao.cursor()
        dados = (str(uuid.uuid4()), cotacao_EUR, cotacao_USD, str(datetime.today().strftime('%y-%m-%d')))
        comando.execute("Insert into Cotacoes(ID, Cotacao_EUR, Cotacao_USD, Data) values(?, ?, ?, ?)", dados)
        conexao.commit()