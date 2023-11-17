# Verificando taxa de retorno diária
from matplotlib.pyplot import plot
import pandas as pd
import numpy as np
import plotly.express as px

dataset = pd.read_csv('acoes.csv')
#print(dataset['Americanas'])
#print(dataset['Americanas'].shift(1))

dataset['RS Americanas'] = (dataset['Americanas']/dataset['Americanas'].shift())-1
#print(dataset)
dataset['RS Americanas'].plot();
print(dataset['RS Americanas'].mean())
