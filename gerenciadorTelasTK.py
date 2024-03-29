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
from tkinter import filedialog, messagebox, ttk
from matplotlib.figure import Figure
from pandastable import Table, TableModel

# Imports  Meus Arquivos
import telas
import analiseMatematica
import megaLimpezaDados



master = Tk() 
master.geometry("1010x710") 
## CORES UTILIZADAS NA TELA PRINCIPAL TK
c1 = '#0d2754'  #Cor do fundo de tela geral
c2 = '#0a0e2e' #Cor de fundo do  Frame
c3 = '#182480' #Cor da borda do Frame
c4 ='#717ff5'  #Cor do fundo de imagem
c5 ='#f5f5f7'  #Cor dos textos branco
c6 = '#e8e6e6' # Cor fundo Frame 2

master.title('JF - DashBoard Mega Sena - Brasil  - UFSC - POO II - 2022-1')
master.configure(bg=c1) #Define a cor de fundo da tela inicial
w = Canvas(master) ## Função para inserir imagens nos Frames

##  CHAMA A PRIMEIRA JANELA DE ANALISES 
def janela1():
    '''Funçao que abre a janela do arquivo telas
    para a primeira analise com o botão1 do frame1'''
    telas.Primeira()
    return

##  CHAMA A SEGUNDA JANELA DE ANALISES 
def janela2():
    '''Funçao que abre a janela do arquivo telas
    para  a segunda analise com botão2 do frame1'''
    telas.Segunda()
    return

##  CHAMA A TERCEIRA JANELA DE ANALISES 
def janela3():
    '''Funçao que abre a janela do arquivo telas
    para a terceira analise como botão3 do frame1'''
    freque = analiseMatematica.Estatistica().FreqNumSorteados(db)
    telas.Terceira().framesScreem(freque)
    

##  CHAMA A TERCEIRA JANELA DE ANALISES 
def janela4():
    '''Funçao que abre a janela do arquivo telas
    para a terceira analise como botão3 do frame1'''
     ## Cria lista de jogos
    kx = (entrada_X.get()).split()
    #entrada_X.delete(0,END) # Depois de pegar os valores apaga o camppo Entry
    x = []
    for item in kx:
        x.append(int(item))
        x.sort()  ## Ordena a lista  do jogo proposto em ordem crescente 
    print(x)
    dadosTabela = db
    funcao, a1, a2, a3, a4, a5, a6  = analiseMatematica.Estatistica().avaliaSorteios(dadosTabela,x) ## retorna quantos  jogos apresentam o resultados positivos de sorteio
    telas.Quarta().framesScreem(x, funcao, a1, a2, a3, a4, a5, a6)  ## Chama a tela 4 de apresentação 

def janela4b():
    '''Funcao que faz mesma analise da janela 4 porem com x
    ultimos sorteios '''
    ## Cria lista de jogos
    kx = (entrada_X.get()).split()
    #entrada_X.delete(0,END) # Depois de pegar os valores apaga o camppo Entry
    x = []
    for item in kx:
        x.append(int(item))
        x.sort()  ## Ordena a lista  do jogo proposto em ordem crescente 
    print(x)
    # Captura o tamanho da amostra e gera dataframe
    pg = (entrada_X2.get())
    entrada_X2.delete(0,END)
    lg = int(pg)
    dtfAmostra = db.tail(lg)
    dadosTabela2 = db
    #Chama função de alise com dataframe menor
    funcao2, b1, b2, b3, b4, b5, b6  = analiseMatematica.Estatistica().avaliaSorteios(dtfAmostra,x) ## retorna quantos  jogos 
    telas.Quinta().framesScreem(x, funcao2, b1, b2, b3, b4, b5, b6)  ## Chama a tela 4 de apresentação  com dataset reduzido





def framesScreem ():
        '''Função que define o tamnho e a posição dos frames'''
        # FRAME 1  Barra Lateral da tela Main
        ###  =-=-=-=-=- FRAME 01 =-=-=-=-=-=-=-=
        frame1 = Frame(master, bd=4 ,bg=c2, highlightbackground=c3, highlightthickness=3)
        frame1.place(relx=0.01, rely=0.07, relwidth=0.25, relheight=0.92)
       
        ###  =-=-=-=-=- FRAME 01  CONTEUDO =-=-=-=-=-=-=-=
        ## LABEL 1  -  Frame 1
        tex1 = Label(frame1, text ='Análise de jogos com 06 numeros sorteados \
            que premiaram com 06 acertos', font=('nimbus sans l', 8), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex1.place(relx=0.05, rely=0.05)
        ## Botões 1  -   Frame 1
        btn = Button(frame1, text ='Tela 01 ', command = janela1) 
        btn.place (relx = 0.05, rely= 0.10)

        ## LABEL 2  -  Frame 1
        tex2 = Label(frame1, text ='Análise de jogos com 06 numeros sorteados \
            que NÂO houve Ganhadores com 06 acertos', font=('nimbus sans l', 8), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex2.place(relx=0.05, rely=0.15)
        ## Botões 2  -   Frame 1
        btn2 = Button(frame1, text ='Tela 02 ', command = janela2) 
        btn2.place (relx = 0.05, rely= 0.20)

        ## LABEL 3 - Frame 1
        tex3 = Label(frame1, text ='Comparar Jogos anteriores com nova  \
          aposta ', font=('nimbus sans l', 8), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex3.place(relx=0.05, rely=0.25)

        ## Botões 3  -   Frame 1
        btn3 = Button(frame1, text ='Tela 03 ', command = janela3) 
        btn3.place (relx = 0.05, rely= 0.30)

        ## LABEL 3 - Frame 1
        tex4 = Label(frame1, text='Criar um jogo apara avaliação', font=('nimbus sans l', 10), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex4.place(relx=0.05, rely=0.35)
        # Entrada de valores
        global entrada_X  ## Cria uma variável global para uso na funcao janela4
        entrada_X = Entry(frame1, width=28)
        entrada_X.place(relx=0.05, rely=0.40)
        ### BOTAO entra Jogo
        btn4 = Button(frame1, text ='Tela 04 ', command = janela4) 
        btn4.place (relx = 0.05, rely= 0.45)

        ## Fazer o mesmo teste com os ultimos X jogos
        explic = f'Vamos realizar o mesmo teste acima ( de todos os jogos neste dataset) para os  "X" ultimos jogos :'
        tex4 = Label(frame1, text = explic, font=('nimbus sans l', 9), fg=c5, bg=c2, justify='left', wraplength= 240)
        tex4.place(relx=0.05, rely=0.50)
        ## entrada do tamanho da amostra
        global entrada_X2  ## Cria uma variável global para uso na funcao janela4
        entrada_X2 = Entry(frame1, width=15)
        entrada_X2.place(relx=0.05, rely=0.60)
        ### BOTAO entra tamanho amostra
        btn4 = Button(frame1, text ='Tela 05 ', command = janela4b) 
        btn4.place (relx = 0.55, rely= 0.59)

        ###  =-=-=-=-=- FRAME 02 =-=-=-=-=-=-=-=
        # FRAME 2 Area de visualização dos dados do programa
        frame2 = Frame(master, bd=4 ,bg=c6, highlightbackground=c3, highlightthickness=3)
        frame2.place(relx=0.27, rely=0.07, relwidth=0.72, relheight=0.48)

        ## Imagem do Logo UFSC
        logo1 = PhotoImage(file= r"ima/logoUfscRd1.png")  ## Caminho realtivo da imagem a ser inserida
        w.create_image(0,0, image=logo1) ## Cria a imagem para inserção
        w.image = logo1 ## Copia o arquivo da imagem gerada no logo1
        labLogo1 = Label(frame2, image= w.image) ## Label onde será colocado a imagem
        labLogo1.place(relx=0.00, rely=0.00)

        #####   TEXTO FRAME 02 
        ## LABEL 3 - Frame 1
        global da,db
        da, db = gerando()
        tamanho = len(da)
        ###
        frase_01 = f' O presente dataset de dados, é retirado do site da Caixa Econômica Federal, na página de resultados dos sorteios da Mega Sena. O presente dataset contem  {tamanho}  jogos para serem analisados.'
        ###
        # Impressao no frame 2 do dataset completo
        ###
        # Texto inicial 
        tex5 = Label(frame2, text= frase_01, font=('nimbus sans l', 14), fg=c1, bg=c6, justify='left', wraplength= 450)
        tex5.place(relx=0.28, rely=0.08)
        # Amostra dataset
        frame3 = Frame(master,bd=4 ,bg=c6, highlightbackground=c3, highlightthickness=3)
        frame3.place(relx=0.27, rely=0.51, relwidth=0.72, relheight=0.48)
        table = pt = Table(frame3, dataframe=da,
                                showtoolbar=True, showstatusbar=True) # Este comando gera a tabela do dataframe completo na tela
        pt.show()
        

        # DATA 
def gerando():
    ## Textos com dados dos dataframes
    # Buscando DataFrames
    inicio  = analiseMatematica.Estatistica()
    completo = inicio.df0 ## >> Dataframe completo
    # Gerar Data frame completo filtrado so as dezenas
    jogos = megaLimpezaDados.PuxaCSV().retira(completo) ## DataFrame somente com as dezenas sorteadas completas 
   
    return (completo, jogos)



framesScreem() ## Função que gera os frames na tela Master do Tkinter

label1= Label(master, text ='Janela Principal Mega Sena - POO II ', font=('nimbus sans l', 12), fg=c5, bg=c1) 
label1.place(relx=0.40, rely=0.01)

mainloop() 
