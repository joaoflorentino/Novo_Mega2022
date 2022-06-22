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
        #dfresult.sort_values(['Frequencia'], ascending=True)
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



class Graficos():
    ''' Classe responsável por gerar os graficos para os 
    dash boards'''
    def __init__(self) -> None:
        pass

    def histogramaMega(self, dfm):
        self.dfGraf = dfm
        num = len(self.dfGraf.index)
        fig, ax = plt.subplots(figsize=(20,15))
        sns.barplot(  x = self.dfGraf.index, y= "Frequencia", palette="rocket", data=self.dfGraf)
        ax.set_title('Frequencia dos Numeros Sorteados ', fontsize=20)
        ax.yaxis.set_label_text('Frequencia ', fontdict={'size':14})
        plt.show()



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

    Max = teste1.nMaiores(freq,10)
    print()
    print(Max)

    Min = teste1.nMenores(freq,10)
    print()
    print(Min)

    graf1 = Graficos()
    graf1.histogramaMega(Max)
    #perdedores = teste1.dataframePerdedores()
    #print(perdedores)

   
   
'''
    est_venc = teste1.estatisticoData(ganhadores)
    print (est_venc)
    print()

    est_perd = teste1.estatisticoData(perdedores)
    print(est_perd)
    
'''
print(f'======== F I M  dos TESTES =============')
print()