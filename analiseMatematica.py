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

from operator import index
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

    def avaliaSorteios(self, dfm, lst):
        ''' Função que compara linha a linha de um dataframe
        para verificar se há iguais - Ja sorteado'''
        self.dataframe = dfm ## Recebe um data frame para analise
        self.lista = lst  ## recebe uma lista de 06 numeros para comparação
        ### A 1
        i = 0
        self.a = self.dataframe.loc[self.dataframe['dezena1'] == self.lista[i]] 
        k = len(self.a)
        self.b= self.a.loc[self.a['dezena2'] == self.lista[i+1]]
        l = len(self.b)
        self.c = self.b.loc[self.b['dezena3'] == self.lista[i+2]]
        m = len(self.c)
        self.d = self.c.loc[self.c['dezena4'] == self.lista[i+3]]
        n = len(self.d)
        self.e = self.d.loc[self.d['dezena5'] == self.lista[i+4]]
        o = len(self.e)
        self.f = self.e.loc[self.e['dezena6'] == self.lista[i+5]]
        p = len(self.f)
        
        if  p == 0:
            resultado = f'SEM acertos'
        else:
            resultado = f'Já ocorreu este Jogo {p}  vez (s)'
        return (resultado, k, l, m, n, o,p)

    def paresImpares(self,dtf):
        '''Funcao que avalia quantos pares e impares no data frame '''
        #self.data = self.FreqNumSorteados(dtf)
        self.data = dtf
        pares = 0
        impares = 0 
        for i in range(1, 60, 2):
            pares = pares + self.data.iloc[i]
        for j in range(0, 60, 2):
            impares = impares + self.data.iloc[j]
        pares = pares + self.data.iloc[59]
        print(f'Pares = {pares[0]}' )
        print(f'Impares = {impares[0]}')
        print(f'Soma dos numeros Sorteadors = {pares[0] + impares[0]}')
        qtpar = pares[0]
        qtimpar = impares[0]

        return (qtpar, qtimpar)

        

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

    def pizzaParImpar(self, qtP, qtI):
        '''Funcão para grafico de pizza par e impar'''
        self.qtPar = qtP
        self.qtImpar = qtI
        cores = ['#bf777f', '#91b597']
        nomes = ['Pares', 'Impares']
        valores = [self.qtPar, self.qtImpar]
        fig, ax =  plt.subplots(figsize=(8,8))
        explode = (0.1, 0)
        ax.pie(valores, labels=nomes, autopct='%.1f%%', shadow= True, explode=explode, colors=cores, startangle=60, radius=1.1, textprops={'fontsize': 22})
        ax.set_title('Pares e Impares nos sorteios' , fontsize = 25)
        fit = plt.savefig("graficos/pizzaPI.png")

#####  MAIN  - Testes ######
if  __name__ == '__main__':
    print(f'************Inicio dos testes deste arquivo**************')
    teste1 = Estatistica()
# Gerar Data frame completo filtrado

    dtf0 = teste1.df0 # data frame completo 
    dtf1 = megaLimpezaDados.PuxaCSV().retira(dtf0) ## DataFrame somente com as dezenas sorteadas completas 
    print(dtf1)
    print('****************************')
    teste1.paresImpares(dtf1)

    

    '''
    ganhadores = teste1.dataframeVencedores()
    print(ganhadores)

    valores1 = ganhadores.value_counts(ganhadores["dezena1"])
    print(valores1)

   
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

  
    ## Teste função Avalia sorteios
   # apst = [9,23,25,37,39,55]
    apst = [9,23,32,35,46,57]
    sera = teste1.avaliaSorteios(dtf1 ,apst)
    print(f'Resultado para esta aposta')
    print(sera)

    '''
    print(f'======== F I M  dos TESTES =============')
    print()