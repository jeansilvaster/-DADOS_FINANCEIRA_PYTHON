import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import yfinance as yf

# Lista de tickers das ações desejadas
tickers = ["AMER3.SA", "CVCB3.SA", "WEGE3.SA", "MGLU3.SA", "BOVA11.SA"]

# Baixar dados
dados = yf.download(tickers, start="2020-01-01", end="2023-01-01")['Close']

# Exibir os primeiros registros dos dados
#print(dados.head())

dados = dados.rename(columns={'AMER3.SA' : 'Americanas','CVCB3.SA' : 'CVC', 'WEGE3.SA' : 'WEG', 'MGLU3.SA' : 'MAGALU', 'BOVA11.SA' : 'Ibovespa' })

#print(dados)
#dados.plot(figsize=(15,10), title='Histórivos das ações');

dados_normalizados =dados.copy()
for i in dados_normalizados.columns[0:]:
    dados_normalizados[i] = dados_normalizados[i]/dados_normalizados[i][0]

figura = px.line(title='Histórico dos preços das ações')
for i in dados.columns[1:]:
    figura.add_scatter(x=dados.index, y=dados[i], name=i)
    figura.show()

    figura2 = px.line(title='Histórico dos preços das ações(normalizados)')
    for j in dados_normalizados[1:]:
        figura2.add_scatter(x=dados.index, y=dados_normalizados[j], name=j)
figura2.show()        
