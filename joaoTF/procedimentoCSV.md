![AssinaturaPython-2022](https://github.com/joaoflorentino/Novo_Mega2022/blob/main/figs/AssinaturaPython-2022-Small.png)


## <font color= green>Procedimentos com as planilhas .csv baixada site loterias caixa</font>
***
❇️ Na pagina da Caixa { https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx }  salvar como arquivo html;<br>
❇️ Usando a planilha do google, abrir nova planilha e escolher a opção de importar (em arquivo) e importar o arquivo HTML salvo;<br>
❇️ Nesta planilha, remover as linhas no inicio da planilha que não fazerm parte da análise deixando apenas os títulos das colunas e trocando os títulos das dezenas e do numero de premiados; <br>
❇️ Remover as colunas desnecessárias deixando apenas as colunas:<br>
- Concurso
- Data
- dezena1
- dezena2
- dezena3
- dezena4
- dezena5
- dezena6
- Mega -> <font color=ligblue>quantas apostas venceram o concurso </font>
- Quina -> <font color=ligblue>quantas apostas venceram a quina </font>
- Quadra -> <font color=ligblue>quantas apostas venceram a quadra </font>
- Cidade -> <font color=ligblue>Cidade em que venceram a mega   </font><br>

Feitas estas alterações (limpezas) salvar o arquivo como mega.csv e coloca-lo na pasta /data
