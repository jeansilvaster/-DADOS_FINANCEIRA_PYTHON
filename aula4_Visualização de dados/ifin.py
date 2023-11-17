import yfinance as yf
import pandas as pd

# Lista de tickers das ações desejadas
tickers = ["AMER3.SA", "CVCB3.SA", "WEGE3.SA", "MGLU3.SA", "BOVA11.SA"]

# Baixar dados
dados = yf.download(tickers, start="2020-01-01", end="2023-01-01")

# Exibir os primeiros registros dos dados
print(dados.head())
