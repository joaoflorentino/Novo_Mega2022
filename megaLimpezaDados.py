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
        self.dataFrame = pd.read_csv(self.caminho, index_col='Conc.')
        return self.dataFrame.head(5)
      

df0 = PuxaCVS()
cabec = df0.buscarCvs()
print(cabec)
