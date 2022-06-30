'''
Este programa tem o objetivo de criar um estudo sobre os resultados
dos jogos da mega sena que, neste momento da criação dos scripts, 
são desde o inicio dos jogos (sorteios) até o joto numero  2470 de 
abril de 2022.

Este estudo Gerencia as Janelas do Tkinter. 

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
# Imports  Meus Arquivos
import megaDashboard as md

master = Tk() 
master.geometry("1650x900") 
c1 = '#0d2754'  #Cor do fundo de tela geral
c2 = '#0a0e2e' #Cor de fundo do  Frame
c3 = '#182480' #Cor da borda do Frame
c4 ='#717ff5'  #Cor do fundo de imagem
c5 ='#f5f5f7'  #Cor dos textos

master.title('JF - DashBoard Mega Sena - Brasil  / 2022')
master.configure(bg=c1)

def openNewWindow(): 
    '''Fução Janela main'''
    T1 = md.Telatk()
    
    newWindow = Toplevel(T1) 

label = Label(master, text ="This is the main window") 

label.pack(pady = 10) 
btn = Button(master, text ="Click to open a new window",  command = openNewWindow) 
btn.pack(pady = 10) 
mainloop() 
