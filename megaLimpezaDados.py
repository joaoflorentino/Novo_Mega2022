# *-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Limpeza inicial dos dados de sorteio planinha
# de jogos  .csv  com sorteios ate abril 2022 
# João Florentino  -  Python 2022
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''
Est programa Python, conforme README.md  avalia os últimos sorteios
da Megasenna onde um jogador faz uma aposta de 06 números e recebe
um prémio a partir de 04 acertos até o prémio total com 06 acertos. 

Com os dados dos sorteios desde o inicio do jogo até (por hora) Abril de 
2022 vou fazer algumas abordagens sobre os resultados dos sorteios. 

'''

# IMPORTAÇOES 

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime
from IPython.core.display import HTML

## Classes 

class PuxaCVS:
    def __init__(self) -> None:
        self.caminho = 'data/mega.csv'
        

    def buscarCvs(self):
        '''Funcao de busca de arquivo csv contendo sorteios
        da megasena '''
        self.dataFrame = pd.read_csv(self.caminho, index_col='Conc.')
        return self.dataFrame.head(5)

    def faxinaData(self):
        '''Funçao cria novo dataframe com elininação dos dados
        NdN contidos no frame inicial '''
        self.df1 = self.dataFrame.sort_values(['Conc.'], ascending=True)
        self.df1.fillna(value=0,  inplace=True)
        return self.df1.head(8)

    def criaListaSorteio(self):
        '''Funcao que elimina algumas colunas deixando as dezenas sorteadas
       e o numero do concurso '''
        self.sort = []
        self.df2 = self.df1.drop(['Data', 'Ganhador', 'premio'], axis=1) 
        return self.df2

    def criaArquivosDeEstudos(self):
        self.df1.to_csv('data/organizadoDf1.csv')
        self.df2.to_csv('data/concursosDezenas.csv')

        return

if __name__ == '__main__':

    df0 = PuxaCVS()
    cabec = df0.buscarCvs()
    print(cabec)
    inverte = df0.faxinaData()
    print(inverte)
    dezenas = df0.criaListaSorteio()
    print(dezenas)
    print(f'Salvando arquivos para outros estudos subsequentes:')
    #df0.criaArquivosDeEstudos()


