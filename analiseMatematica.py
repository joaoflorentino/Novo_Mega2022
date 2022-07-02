# *-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Avaliação matemática  e graficos dos dados de sorteio planinha
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
Busca os dataframes criados em megaLimpezaDados.py
e cria bases matemáticas para  das demais classes do 
programa
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''

# IMPORTAÇOES 

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import seaborn as sns
# > Meus arquivos
import megaLimpezaDados

##  CLASSES     

class Estatistica():
    '''Classe contendo varias analises estatisticas provendo 
    de dataframes criados em pandas'''
    def __init__(self) -> None:
        self.df0 = megaLimpezaDados.PuxaCSV().buscarCsv()

    def estatisticoData(self,dfm):
        '''Faz coleta estatistica do dataframe pandas'''
        self.estdata = dfm.describe()
        return self.estdata
    
    ### Dataframe com vencedores da sena 
    def dataframeVencedores(self):
        '''Separa os Vencedores da mega sena '''
        df1 = self.df0.loc[self.df0['Mega'] > 0]
        dfVenc = megaLimpezaDados.PuxaCSV().frameUm(df1)
        return dfVenc
    ### Dataframe com Perdedores da sena 
    def dataframePerdedores(self):
        '''Separa os Pededores da mega sena '''
        df1 = self.df0.loc[self.df0['Mega'] == 0]
        dfPerds = megaLimpezaDados.PuxaCSV().frameUm(df1)
        return dfPerds
    
    def FreqNumSorteados(self,dtfm):
        '''Funcao que determina a frequencia de numeros 
        vencedores no dataFrame'''
        self.dfava = dtfm
        TotalDasDezenas = self.dfava.apply(pd.Series.value_counts)
        TotalDasDezenas.fillna(value=0,  inplace=True) 
        dfresult = TotalDasDezenas
        dfresult["Frequencia"] = dfresult[list(dfresult.columns)].sum(axis=1) 
        
        freq = dfresult[['Frequencia']]
        return freq

    def nMaiores(self,dfm,n):
        '''Funcção que determinas os n Maiores valores da 
        frequencia de sorteio'''
        self.dataFamePand = dfm
        self.nval = n
        Maiores = self.dataFamePand.nlargest(self.nval, ['Frequencia'])
        return (Maiores)

    def nMenores(self,dfm,n):
        '''Funcção que determinas os n Menores valores da 
        frequencia de sorteio'''
        self.dataFamePand = dfm
        self.nval = n
        Menores = self.dataFamePand.nsmallest(self.nval, ['Frequencia'])
        return (Menores)


##  Outa Classe  Graficos
class Graficos():
    ''' Classe responsável por gerar os graficos para os 
    dash boards'''
    def __init__(self) -> None:
        pass

    def barrasMega(self, dfm,tituloGra):
        '''Função que cria grafico de barras Seaborn '''
        self.dfGraf = dfm
        self.tit = tituloGra # Titulo do grafico vem da chamada da função
        ## Abaixo cria-se um grafico de barras seaborn ordenando os numeros dos menos sorteados para os mais 
        sns.set_context("notebook", font_scale=1.8)  ## Define o contexto do seaborn para melhorar a visualização
        fig, ax = plt.subplots(figsize=(12,10))## Gera o tamanho da imagem do grafico
        sns.barplot(  x = self.dfGraf.index, y= "Frequencia", palette="icefire", data=self.dfGraf, order=self.dfGraf.sort_values('Frequencia').index)
        ax.set_title(self.tit, fontsize=20)
        ax.set_xlabel('Numeros Sorteados', fontsize = 20)
        ax.yaxis.set_label_text('Frequencia ', fontdict={'size':18})
        plt.tight_layout()
        #plt.show()
        fi = plt.savefig('graficos/bar1.png')
        return (fi)
    
    def histogramaMega(self,dtf, tituloGr):
        '''Função que gera um histograma de um dataFrame'''
        self.dataFrame = dtf # Carrega o dataframe
        self.titu = tituloGr # Titulo do grafico vem da chamada da função
        ## Abaixo cria-se um histograma com curva normal seaborn com a frequencia dos numeros sorteados
        sns.set_context("notebook", font_scale=1.8) ## Define o contexto do seaborn para melhorar a visualização
        fig, ax = plt.subplots(figsize=(12,10)) ## Gera o tamanho da imagem do grafico
        sns.histplot(self.dataFrame, x='Frequencia', kde=True, ax=ax ) ## KDE gera a curva normal no histograma
        ax.set_xlabel('Frequencia dos numeros', fontsize = 20)
        ax.set_title(self.titu, fontsize=20) 
        ax.yaxis.set_label_text('Probabilidade ', fontdict={'size':18})
        plt.tight_layout()

        #plt.show()
        fih = plt.savefig("graficos/histog01.png")
        return (fih)

#####  MAIN  - Testes ######
if  __name__ == '__main__':
    print(f'************Inicio dos testes deste arquivo**************')
    teste1 = Estatistica()
    ganhadores = teste1.dataframeVencedores()
    print(ganhadores)

    #valores1 = ganhadores.value_counts(ganhadores["dezena1"])
    #print(valores1)
    freq = teste1.FreqNumSorteados(ganhadores)
    freq.sort_values(['Frequencia'], ascending=True)
    print(freq)
    print()
    est_freq = teste1.estatisticoData(freq)
    print(est_freq)

    Max = teste1.nMaiores(freq,25)
    print()
    print(Max)

    Min = teste1.nMenores(freq,10)
    print()
    print(Min)

    graf1 = Graficos()
    graf1.barrasMega(Max)
    graf1.histogramaMega(Max)
    plt.show()
    
    
    #perdedores = teste1.dataframePerdedores()
    #print(perdedores)
    print(f'======== F I M  dos TESTES =============')
    print()