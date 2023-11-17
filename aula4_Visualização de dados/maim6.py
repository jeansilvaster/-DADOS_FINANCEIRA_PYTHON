import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px


azul_df = data.DataReader(name='AZUL4.SA', data_source='yahoo', start="2022-01-01", end="2023-07-31")
print(azul_df.info())



   


