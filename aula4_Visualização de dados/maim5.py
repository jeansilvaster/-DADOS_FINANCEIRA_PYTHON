#Aula 03 – Análise de dados e estatística básica
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
import yfinance as yfin
yfin.pdr_override()


#azul_df = data.DataReader(name='AZUL4.SA', data_source='yahoo',start='2023-03-10')
#print(azul_df)

azul_df = pdr.get_data_yahoo("AZUL4.SA", start="2022-01-01", end="2023-07-31")
#print(azul_df.info())
#print(azul_df.head(3))
#print(azul_df.tail(4))
#print(azul_df.describe())
#print(azul_df[azul_df['Close'] >= 39.21])
#print(azul_df[azul_df['Close'] >= 10.35])
#print(azul_df[(azul_df['Close'] >=10.34) & (azul_df['Close'] <=10.36)])
azul_df.to_csv('azul.csv')
print("dados salvos com sucesso!")