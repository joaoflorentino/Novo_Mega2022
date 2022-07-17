'''
Este programa tem o objetivo de criar um estudo sobre os resultados
dos jogos da mega sena que, neste momento da criação dos scripts, 
são desde o inicio dos jogos (sorteios) até o joto numero  2470 de 
abril de 2022.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Este arquivo gerencia a abertura das novas telas do TKinter 
a função janela  X vai abrindo as novas janelas de acordo a proposta
da aplicação
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

# ******************************************
# Projeto análise estatistica Jogo Mega Sena
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 

from tkinter import *
import tkinter.font  as tkF
from matplotlib.figure import Figure

# Imports  Meus Arquivos
import telas
import analiseMatematica
import megaLimpezaDados


master = Tk() 
master.geometry("1000x500") 
## CORES UTILIZADAS NA TELA PRINCIPAL TK
c1 = '#0d2754'  #Cor do fundo de tela geral
c2 = '#0a0e2e' #Cor de fundo do  Frame
c3 = '#182480' #Cor da borda do Frame
c4 ='#717ff5'  #Cor do fundo de imagem
c5 ='#f5f5f7'  #Cor dos textos
c6 = '#e8e6e6' # Cor fundo Frame 2

master.title('JF - DashBoard Mega Sena - Brasil  - UFSC - POO II - 2022-1')
master.configure(bg=c1) #Define a cor de fundo da tela inicial
w = Canvas(master) ## Função para inserir imagens nos Frames

##  CHAMA A PRIMEIRA JANELA DE ANALISES 
def janela1():
    '''Funçao que abre a janela do arquivo telaUmV2
    para o botão do frame1'''
    telas.Primeira()
    return

##  CHAMA A PRIMEIRA JANELA DE ANALISES 
def janela2():
    '''Funçao que abre a janela do arquivo telaUmV2
    para o botão do frame1'''
    telas.Segunda()
    return

def framesScreem ():
        '''Função que define o tamnho e a posição dos frames'''
        # FRAME 1  Barra Lateral da tela Main
        frame1 = Frame(master, bd=4 ,bg=c2, highlightbackground=c3, highlightthickness=3)
        frame1.place(relx=0.01, rely=0.07, relwidth=0.25, relheight=0.92)



        ## LABEL 1  -  Frame 1
        tex1 = Label(frame1, text ='Análise de jogos com 06 numeros sorteados \
            que premiaram com 06 acertos', font=('nimbus sans l', 8), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex1.place(relx=0.01, rely=0.01)
        ## Botões 1  -   Frame 1
        btn = Button(frame1, text ='Tela 01 ', command = janela1) 
        btn.place (relx = 0.05, rely= 0.12)

        ## LABEL 2  -  Frame 2
        tex2 = Label(frame1, text ='Análise de jogos com 06 numeros sorteados \
            que NÂO houve Ganhadores com 06 acertos', font=('nimbus sans l', 8), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex2.place(relx=0.05, rely=0.20)
        ## Botões 1  -   Frame 1
        btn2 = Button(frame1, text ='Tela 02 ', command = janela2) 
        btn2.place (relx = 0.05, rely= 0.30)



        # FRAME 2 Area de visualização dos dados do programa
        frame2 = Frame(master, bd=4 ,bg=c6, highlightbackground=c3, highlightthickness=3)
        frame2.place(relx=0.27, rely=0.07, relwidth=0.72, relheight=0.92)

        ## Imagem do Logo UFSC
        logo1 = PhotoImage(file= r"ima/logoUfscRd1.png")  ## Caminho realtivo da imagem a ser inserida
        w.create_image(0,0, image=logo1) ## Cria a imagem para inserção
        w.image = logo1 ## Copia o arquivo da imagem gerada no logo1
        labLogo1 = Label(frame2, image= w.image) ## Label onde será colocado a imagem
        labLogo1.place(relx=0.01, rely=0.01)

        '''
        ## Textos com dados dos dataframes
        # Buscando DataFrames
        df0 = megaLimpezaDados.PuxaCSV.buscarCsv()
        # DATA 1
        df1a = megaLimpezaDados.PuxaCSV.criaListaSorteio()
        df1 = megaLimpezaDados.PuxaCSV.faxinaData(df1a)
        # DATA 2

        '''
        



framesScreem() ## Função que gera os frames na tela Master do Tkinter

label1= Label(master, text ='Janela Principal Mega Sena - POO II ', font=('nimbus sans l', 12), fg=c5, bg=c1) 
label1.place(relx=0.40, rely=0.01)

mainloop() 
