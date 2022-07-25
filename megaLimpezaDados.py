# *-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Limpeza inicial dos dados de sorteio planinha
# de jogos  .csv  com sorteios ate junho 2022 
# João Florentino  -  Python 2022
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''
Est programa Python, conforme README.md  avalia os últimos sorteios
da Megasenna onde um jogador faz uma aposta de 06 números e recebe
um prémio a partir de 04 acertos até o prémio total com 06 acertos. 

Com os dados dos sorteios desde o inicio do jogo até (por hora) Abril de 
2022 vou fazer algumas abordagens sobre os resultados dos sorteios. 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
baseCSV - cria dataframes Pandas para uso das demais classes do 
programa
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''

# IMPORTAÇOES 

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime


## Classes 

class PuxaCSV:
    '''Classe que retorna DataFrames Pandas organizados para uso das 
    demais classes do programa '''

    def __init__(self) -> None:
        self.caminho = 'data/mega.csv'
        

    def buscarCsv(self):
        '''Funcao de busca de arquivo csv contendo sorteios
        da megasena '''
        self.dataFrame = pd.read_csv(self.caminho, index_col='Concurso')
        self.df0 = self.faxinaData(self.dataFrame)
        return self.df0

    ###DataFrame 01 
    def frameUm(self,dfm):
        '''Cria Primeiro Data frame com numero de sorteio e 
        dezenas sorteadas em ordem crescente'''
        df1 = dfm.iloc[:, [1,2,3,4,5,6]] #Comando para separar as colunas que necessito inicialmente no estudo
        df2 = self.faxinaData(df1)
        return df2
    
    ### DataFrame 02
    
    def faxinaData(self,df0):
        '''Funçao cria novo dataframe com elininação dos dados
        NdN contidos no frame inicial '''
        self.dataFrame = df0
        self.df = self.dataFrame.sort_values(['Concurso'], ascending=True)
        self.df.fillna(value='',  inplace=True)  #Retira todos NaN do dataframe
        return self.df

    def retira(self, dtf):
        "Funcao Retira colunas"
        self.d = dtf
        self.resultado = self.d.drop(['Data', 'Mega', 'Quina', 'Quadra', 'Cidade'], axis = 1)
        return self.resultado

    def criaArquivosDeEstudos(self):
        self.df1.to_csv('data/organizadoDf1.csv')
        self.df2.to_csv('data/concursosDezenas.csv')

        return


#####  MAIN  - Testes ######
if __name__ == '__main__':
    print(f'_+_+_+_+_+_+_+_   Inicio deste TESTE =-=-=-=-=-=-=-=-=-=-=-=')
    df0 = PuxaCSV()
    cabec = df0.buscarCsv()
    cabec.info()
    print(cabec)
    print(cabec.isnull().sum())
    limpoNaN = df0.faxinaData(cabec) ## Limpa todo DataFrame de NaN
    print(limpoNaN) ## mostra limpeza do DataFrame

    
    print()
    print('Analise dataFraem 01 informações do Pandas')
    primeiro = df0.frameUm(limpoNaN)
    #print(primeiro)
    primeiro.info()
    #primeiro.tail(10)
    #print(primeiro.isnull().sum()) # Informa se há valores nulos nas colunas e soma em cada coluna quantos são

    print(primeiro.describe()) ## Descreve estatisticamente os valores dos sorteios das dezenas 
    k = primeiro['dezena1'].describe() ## valores estatisticos da primeira dezena
    print(f'{k}')
    print(f'*-*-*-*-*-*-*-*-*-Fim das Informações do pandas Data Frame 01*-*-*-*-*-*-*-*-*-*-*')
    print()
    

    
    """    
    inverte = df0.faxinaData()
    print(inverte)
    dezenas = df0.criaListaSorteio()
    print(dezenas)
    print(f'Salvando arquivos para outros estudos subsequentes:')
    #df0.criaArquivosDeEstudos()
    
    """
    


