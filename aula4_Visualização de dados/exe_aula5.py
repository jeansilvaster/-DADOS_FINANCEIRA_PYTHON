import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Lista de tickers das ações
tickers = ['BBDC4.SA', 'BBAS3.SA', 'NUBANK', 'ITUB4.SA', 'CXSE3.SA', 'BOVA11.SA']

# Defina o intervalo de datas
start_date = '2019-03-01'
end_date = '2021-12-31'

# Crie um DataFrame para armazenar os dados de cada ação
df = pd.DataFrame()

# Faça o download dos dados do Yahoo Finance
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    df[ticker] = data['Adj Close']

# Normalize os dados
normalized_df = df / df.iloc[0]

# Plot usando Matplotlib
normalized_df.plot(figsize=(10, 6))
plt.title('Desempenho Normalizado das Ações (Matplotlib)')
plt.xlabel('Data')
plt.ylabel('Preço Normalizado')
plt.show()

# Plot usando Seaborn
sns.set_theme()
plt.figure(figsize=(10, 6))
sns.lineplot(data=normalized_df)
plt.title('Desempenho Normalizado das Ações (Seaborn)')
plt.xlabel('Data')
plt.ylabel('Preço Normalizado')
plt.show()

# Plot usando Plotly
fig = px.line(normalized_df, x=normalized_df.index, y=normalized_df.columns, title='Desempenho Normalizado das Ações (Plotly)')
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Preço Normalizado')
fig.show()

# Calcule o retorno total para cada ação
total_return = normalized_df.iloc[-1] - 1

# Encontre a ação mais rentável
acao_mais_rentavel = total_return.idxmax()
retorno_mais_rentavel = total_return.max()

print(f"A ação mais rentável foi {acao_mais_rentavel} com um retorno total de {retorno_mais_rentavel:.2%}")
