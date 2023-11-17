# Verificando taxa de retorno simples
import pandas as pd
import numpy as np
import plotly.express as px

dataset = pd.read_csv('acoes.csv')
#print(dataset.shape)
#print(dataset)

#print(dataset['Americanas'][0])
#print(dataset['Americanas'][len(dataset)-1])

rs_amaericanas = ((dataset['Americanas'][len(dataset)-1]-dataset['Americanas'][0])/dataset['Americanas'][0])*100
print(rs_amaericanas)

rs_CVC = ((dataset['CVC'][len(dataset)-1]-dataset['CVC'][0])/dataset['CVC'][0])*100
print(rs_CVC)

rs_WEG = ((dataset['WEG'][len(dataset)-1]-dataset['WEG'][0])/dataset['WEG'][0])*100
print(rs_WEG)

rs_MAGALU = ((dataset['MAGALU'][len(dataset)-1]-dataset['MAGALU'][0])/dataset['MAGALU'][0])*100
print(rs_MAGALU)

# forma reduzida

rs_CVC_re = (dataset['CVC'][len(dataset)-1]/dataset['CVC'][0]-1)*100
print(rs_CVC_re)