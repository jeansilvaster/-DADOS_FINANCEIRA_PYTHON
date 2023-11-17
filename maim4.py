#Aula 03 – Manipulação de dados com Ações Financeiras
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
import yfinance as yfin
yfin.pdr_override()


azul_df = pdr.get_data_yahoo("AZUL4.SA", start="2022-01-01", end="2023-07-31")
#print(azul_df.info())
print(azul_df.head(3))


