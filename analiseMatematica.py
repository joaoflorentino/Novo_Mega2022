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
        
    





class Graficos():
    pass



#####  MAIN  - Testes ######
if  __name__ == '__main__':
    print(f'************Inicio dos testes deste arquivo**************')
    teste1 = Estatistica()
    ganhadores = teste1.dataframeVencedores()
    print(ganhadores)
    perdedores = teste1.dataframePerdedores()
    print(perdedores)

    est_venc = teste1.estatisticoData(ganhadores)
    print (est_venc)
    print()

    est_perd = teste1.estatisticoData(perdedores)
    print(est_perd)
    print(f'======== F I M  dos TESTES =============')
    print()
