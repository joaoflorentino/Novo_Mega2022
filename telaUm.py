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
from PIL import ImageTk,Image

#import Meus Arquivos

# Importação para colocar o grafico dentro da janela do tkinter
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

## FONTES TTF



##  GUI  
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
        '''Função que posiciona o grafico dentro do frame1'''
        # Grafico FRAME 1
        self.grafo1 = plt.figure(figsize=(5,5),  dpi=100)
        self.canvasG1 = FigureCanvasTkAgg(self.grafo1, master=self.frame1)
        self.figrafico =  self.grafo1.add_subplot(111)
        self.canvasG1.get_tk_widget().place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)
        #self.toobar = NavigationToolbar2Tk(self.canvasG1, self.frame1)
        self.canvasG1._tkcanvas.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97)

        # Grafico FRAME 2
        self.grafo2 = plt.figure(figsize=(5,5),  dpi=100)
        self.canvasG2 = FigureCanvasTkAgg(self.grafo2, master=self.frame2)
        self.figrafico =  self.grafo2.add_subplot(111)
        self.canvasG2.get_tk_widget().place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)
        #self.toobar = NavigationToolbar2Tk(self.canvasG1, self.frame1)
        self.canvasG2._tkcanvas.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97)

        # Grafico FRAME 3
        self.grafo3 = plt.figure(figsize=(5,5),  dpi=100)
        self.canvasG3 = FigureCanvasTkAgg(self.grafo3, master=self.frame3)
        self.figrafico =  self.grafo3.add_subplot(111)
        self.canvasG3.get_tk_widget().place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)
        #self.toobar = NavigationToolbar2Tk(self.canvasG1, self.frame1)
        self.canvasG3._tkcanvas.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97)
        
        # Grafico FRAME 4
        self.grafo4 = plt.figure(figsize=(5,5),  dpi=100)
        self.canvasG4 = FigureCanvasTkAgg(self.grafo4, master=self.frame4)
        self.figrafico =  self.grafo4.add_subplot(111)
        self.canvasG4.get_tk_widget().place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)
        #self.toobar = NavigationToolbar2Tk(self.canvasG1, self.frame1)
        self.canvasG4._tkcanvas.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97)

    def poeLogo(self):
        w = Canvas(self.janela)
        logo1 = PhotoImage(file= r"ima/JFPython.png")
        w.create_image(0,0, image=logo1)
        w.image = logo1
        labLogo1 = Label(self.frame5, image= w.image)
        labLogo1.place(relx=0.01, rely=0.01)

    def janelaUsuario(self):

        lb01 = Label(self.frame5, text='Programa Mega Sena', font=('nimbus sans l', 12), fg=self.c5, bg=self.c2)
        lb01.place(relx=0.35, rely=0.05)