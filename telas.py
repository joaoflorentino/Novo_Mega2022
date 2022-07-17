'''
Este programa tem o objetivo de criar um estudo sobre os resultados
dos jogos da mega sena que, neste momento da criação dos scripts, 
são desde o inicio dos jogos (sorteios) até o joto numero  2470 de 
abril de 2022.

Este estudo cria um dashboard com algumas informações dos sorteios
feito em Python e com uso de varias bibliotecas, como Pandas, Tkinter e 
Matplotlib. 

'''

# ******************************************
# Projeto análise estatistica Jogo Mega Sena
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 

from tkinter import *
import tkinter.font  as tkF
import numpy as np
import pandas as pd
from datetime import datetime
import seaborn as sns
from PIL  import Image

#import Meus Arquivos
import analiseMatematica

# Importação para colocar o grafico dentro da janela do tkinter
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

## FONTES TTF



##  GUI  
## Primeira tela 
class  Primeira():

    def __init__(self) -> None:
        
        self.c1 = '#0d2754'  #Cor do fundo de tela geral
        self.c2 = '#0a0e2e' #Cor de fundo do  Frame
        self.c3 = '#182480' #Cor da borda do Frame
        self.c4 ='#717ff5'  #Cor do fundo de imagem
        self.c5 ='#f5f5f7'  #Cor dos textos
        # Demais funcoes de tela
        self.janela = Toplevel()
        self.janela.title('JF - DashBoard Mega Sena - VENCEDORES - Tela 01 ')
        self.janela.configure(bg=self.c1)
        self.janela.geometry('1350x750')
        self.janela.resizable(True, True)  # Permite a janela ser aumentada ou diminuida tanto em x quanto em  y
        self.janela.maxsize(width=1900, height=950)  # Define o tamanho maximo da tela se acima for True
        self.janela.minsize(width= 1000, height= 500) # Define o tamanho minimo da tela se acima for True
        fontSt1 = tkF.Font(family='figs/dc_s.ttf', size=15)
        self.janela.transient()
        self.janela.focus_force()
        self.janela.grab_set()
        ## Chamando demais funçoes 
        self.framesScreem()
        self.screemGrafico()
        self.poeLogo()
        self.janelaUsuario()

    def framesScreem (self):
        '''Função que define o tamnho e a posição dos frames'''
        # FRAME 1
        self.frame1 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 2
        self.frame2 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame2.place(relx=0.35, rely=0.02, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 3
        self.frame3 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame3.place(relx=0.01, rely=0.51, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 4
        self.frame4 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame4.place(relx=0.35, rely=0.51, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 5
        self.frame5 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame5.place(relx=0.69, rely=0.02, relwidth=0.30, relheight=0.96)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 

        ### Conteudo dos Frames ###
    def screemGrafico(self):
        '''Função que posiciona o grafico dentro dos frames'''
        # Grafico FRAME 1
        graf1 = analiseMatematica.Graficos()
        a, b = self.estGanhaVence()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Frequencia dos Numeros Mais Sorteados ')
        ima = graf1.barrasMega(a, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/bar1.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra01= PhotoImage(file= 'graficos/new.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra01) # chama imagem no canvas
        w.image = gra01 # gera o w imagem para inserção no Label
        grafico = Label(self.frame1, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label

        # Grafico FRAME 2
        graf2 = analiseMatematica.Graficos()
        a, b = self.estGanhaVence()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Curva Normal dos Numeros Mais Sorteados ')
        ima = graf2.histogramaMega(a, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/histog01.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new2.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra02= PhotoImage(file= 'graficos/new2.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra02) # chama imagem no canvas
        w.image = gra02 # gera o w imagem para inserção no Label
        grafico = Label(self.frame2, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label

        # Grafico FRAME 3
        graf3 = analiseMatematica.Graficos()
        a, b = self.estGanhaVence()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Frequencia dos Numeros Menos Sorteados ')
        ima = graf3.barrasMega(b, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/bar1.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new3.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra03= PhotoImage(file= 'graficos/new3.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra03) # chama imagem no canvas
        w.image = gra03 # gera o w imagem para inserção no Label
        grafico = Label(self.frame3, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label
        
        # Grafico FRAME 4
        graf4 = analiseMatematica.Graficos()
        a, b = self.estGanhaVence()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Curva Normal dos Numeros Menos Sorteados ')
        ima = graf4.histogramaMega(b, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/histog01.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new4.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra04= PhotoImage(file= 'graficos/new4.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra04) # chama imagem no canvas
        w.image = gra04 # gera o w imagem para inserção no Label
        grafico = Label(self.frame4, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label

    def poeLogo(self):
        '''Função que insere imagem do logo no frame
        comentarios dos comandos no frame 1 acima'''
        w = Canvas(self.janela)
        logo1 = PhotoImage(file= r"ima/JFPython.png")
        w.create_image(0,0, image=logo1)
        w.image = logo1
        labLogo1 = Label(self.frame5, image= w.image)
        labLogo1.place(relx=0.01, rely=0.01)

    def janelaUsuario(self):

        lb01 = Label(self.frame5, text='Informações  dos Graficos', font=('nimbus sans l', 12), fg=self.c5, bg=self.c2)
        lb01.place(relx=0.35, rely=0.05)
        

        ### Funções De Análise Estatística  #####

    def  estGanhaVence(self):
        a = analiseMatematica.Estatistica()
        ganhadores = a.dataframeVencedores()
        freq = a.FreqNumSorteados(ganhadores)
        freq.sort_values(['Frequencia'], ascending=True)
        est_freq = a.estatisticoData(freq)
        self.Max = a.nMaiores(freq,15) ##  Esse valor de 20 é que define o tamanho da amostra mais sorteados
        self.Min = a.nMenores(freq,15) ## mesmo acima menos sorteados 
        return (self.Max, self.Min)

## Segunda tela
class  Segunda():

    def __init__(self) -> None:
        
        self.c1 = '#0d2754'  #Cor do fundo de tela geral
        self.c2 = '#0a0e2e' #Cor de fundo do  Frame
        self.c3 = '#182480' #Cor da borda do Frame
        self.c4 ='#717ff5'  #Cor do fundo de imagem
        self.c5 ='#f5f5f7'  #Cor dos textos
        # Demais funcoes de tela
        self.janela = Toplevel()
        self.janela.title('JF - DashBoard Mega Sena - SEM VENCEDORES - Tela 02 ')
        self.janela.configure(bg=self.c1)
        self.janela.geometry('1350x750')
        self.janela.resizable(True, True)  # Permite a janela ser aumentada ou diminuida tanto em x quanto em  y
        self.janela.maxsize(width=1900, height=950)  # Define o tamanho maximo da tela se acima for True
        self.janela.minsize(width= 1000, height= 500) # Define o tamanho minimo da tela se acima for True
        fontSt1 = tkF.Font(family='figs/dc_s.ttf', size=15)
        self.janela.transient()
        self.janela.focus_force()
        self.janela.grab_set()
        ## Chamando demais funçoes 
        self.framesScreem()
        self.screemGrafico()
        self.poeLogo()
        self.janelaUsuario()

    def framesScreem (self):
        '''Função que define o tamnho e a posição dos frames'''
        # FRAME 1
        self.frame1 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 2
        self.frame2 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame2.place(relx=0.35, rely=0.02, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 3
        self.frame3 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame3.place(relx=0.01, rely=0.51, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 4
        self.frame4 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame4.place(relx=0.35, rely=0.51, relwidth=0.33, relheight=0.47)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 5
        self.frame5 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame5.place(relx=0.69, rely=0.02, relwidth=0.30, relheight=0.96)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 

        ### Conteudo dos Frames ###
    def screemGrafico(self):
        '''Função que posiciona o grafico dentro dos frames'''
        # Grafico FRAME 1
        graf1 = analiseMatematica.Graficos()
        a, b = self.estPerdeu()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Frequencia dos Numeros Mais Sorteados ')
        ima = graf1.barrasMega(a, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/bar1.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra01= PhotoImage(file= 'graficos/new.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra01) # chama imagem no canvas
        w.image = gra01 # gera o w imagem para inserção no Label
        grafico = Label(self.frame1, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label

        # Grafico FRAME 2
        graf2 = analiseMatematica.Graficos()
        a, b = self.estPerdeu()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Curva Normal dos Numeros Mais Sorteados ')
        ima = graf2.histogramaMega(a, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/histog01.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new2.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra02= PhotoImage(file= 'graficos/new2.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra02) # chama imagem no canvas
        w.image = gra02 # gera o w imagem para inserção no Label
        grafico = Label(self.frame2, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label

        # Grafico FRAME 3
        graf3 = analiseMatematica.Graficos()
        a, b = self.estPerdeu()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Frequencia dos Numeros Menos Sorteados ')
        ima = graf3.barrasMega(b, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/bar1.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new3.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra03= PhotoImage(file= 'graficos/new3.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra03) # chama imagem no canvas
        w.image = gra03 # gera o w imagem para inserção no Label
        grafico = Label(self.frame3, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label
        
        # Grafico FRAME 4
        graf4 = analiseMatematica.Graficos()
        a, b = self.estPerdeu()   # Inicia a função estatistica que cria dataframe
        titulo = str(f'Curva Normal dos Numeros Menos Sorteados ')
        ima = graf4.histogramaMega(b, titulo)  #Gera Grafico mais sorteados  e passa titulo
        iume = Image.open('graficos/histog01.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        res.save('graficos/new4.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra04= PhotoImage(file= 'graficos/new4.png') # gera arquivo no Photoimage
        w.create_image(0,0, image=gra04) # chama imagem no canvas
        w.image = gra04 # gera o w imagem para inserção no Label
        grafico = Label(self.frame4, image=w.image) #Label que vai receber imagem acima 
        grafico.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97) #Posicionamento do Label

    def poeLogo(self):
        '''Função que insere imagem do logo no frame
        comentarios dos comandos no frame 1 acima'''
        w = Canvas(self.janela)
        logo1 = PhotoImage(file= r"ima/JFPython.png")
        w.create_image(0,0, image=logo1)
        w.image = logo1
        labLogo1 = Label(self.frame5, image= w.image)
        labLogo1.place(relx=0.01, rely=0.01)

    def janelaUsuario(self):

        lb01 = Label(self.frame5, text='Informações  dos Graficos', font=('nimbus sans l', 12), fg=self.c5, bg=self.c2)
        lb01.place(relx=0.35, rely=0.05)
        

        ### Funções De Análise Estatística  #####

    def  estGanhaVence(self):
        a = analiseMatematica.Estatistica()
        ganhadores = a.dataframeVencedores()
        freq = a.FreqNumSorteados(ganhadores)
        freq.sort_values(['Frequencia'], ascending=True)
        est_freq = a.estatisticoData(freq)
        self.Max = a.nMaiores(freq,15) ##  Esse valor de 20 é que define o tamanho da amostra mais sorteados
        self.Min = a.nMenores(freq,15) ## mesmo acima menos sorteados 
        return (self.Max, self.Min)

    def  estPerdeu(self):
        ka = analiseMatematica.Estatistica()
        perdedores = ka.dataframePerdedores()
        freq = ka.FreqNumSorteados(perdedores)
        freq.sort_values(['Frequencia'], ascending=True)
        est_freq = ka.estatisticoData(freq)
        self.Max = ka.nMaiores(freq,8) ##  Esse valor de 20 é que define o tamanho da amostra mais sorteados
        self.Min = ka.nMenores(freq,8) ## mesmo acima menos sorteados 
        return (self.Max, self.Min)

## Terceira tela

class Terceira():
    def __init__(self) -> None:
            
            self.c1 = '#0d2754'  #Cor do fundo de tela geral
            self.c2 = '#0a0e2e' #Cor de fundo do  Frame
            self.c3 = '#182480' #Cor da borda do Frame
            self.c4 ='#717ff5'  #Cor do fundo de imagem
            self.c5 ='#f5f5f7'  #Cor dos textos
            # Demais funcoes de tela
            self.janela = Toplevel()
            self.janela.title('JF - DashBoard Mega Sena - Nova Aposta e Sorteios - Tela 03 ')
            self.janela.configure(bg=self.c1)
            self.janela.geometry('1350x750')
            self.janela.resizable(True, True)  # Permite a janela ser aumentada ou diminuida tanto em x quanto em  y
            self.janela.maxsize(width=1900, height=950)  # Define o tamanho maximo da tela se acima for True
            self.janela.minsize(width= 1000, height= 500) # Define o tamanho minimo da tela se acima for True
            fontSt1 = tkF.Font(family='figs/dc_s.ttf', size=15)
            self.janela.transient()
            self.janela.focus_force()
            self.janela.grab_set()
            ## Chamando demais funçoes 
            self.framesScreem()
            self.screemGrafico()
            self.poeLogo()
            self.janelaUsuario()

    def framesScreem (self):
            '''Função que define o tamnho e a posição dos frames'''
            # FRAME 1
            self.frame1 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
            self.frame1.place(relx=0.01, rely=0.02, relwidth=0.33, relheight=0.47)
            #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
            # FRAME 2
            self.frame2 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
            self.frame2.place(relx=0.35, rely=0.02, relwidth=0.33, relheight=0.47)
            #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
            # FRAME 3
            self.frame3 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
            self.frame3.place(relx=0.01, rely=0.51, relwidth=0.33, relheight=0.47)
            #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
            # FRAME 4
            self.frame4 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
            self.frame4.place(relx=0.35, rely=0.51, relwidth=0.33, relheight=0.47)
            #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
            # FRAME 5
            self.frame5 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
            self.frame5.place(relx=0.69, rely=0.02, relwidth=0.30, relheight=0.96)
            #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 




### INICIO DO MAIN PARA TESTES DESTE ARQUIVO ######

if __name__ == '__main__':
    df = Primeira()
    '''data = df.estGanhaVence()
    print (data)'''
    df.screemGrafico()
    plt.show()