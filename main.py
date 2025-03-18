# Importa a biblioteca numpy, que é usada para operações matemáticas e manipulação de arrays.
import numpy as np
# Importa a biblioteca pandas, que é usada para manipulação e análise de dados.
import pandas as pd
# Importa a classe SimpleImputer do módulo sklearn.impute, que é usada para preencher valores ausentes em um conjunto de dados.
from sklearn.impute import SimpleImputer

# Lê um arquivo CSV chamado 'data_jobs.csv' e armazena os dados em um DataFrame do pandas.
baseDeDados = pd.read_csv('data_jobs.csv')

# Seleciona todas as linhas e colunas do DataFrame e armazena os valores em um array numpy.
x = baseDeDados.iloc[:,:].values # Pegando as linhas do excel.

# Cria um objeto SimpleImputer que substituirá os valores ausentes (np.nan) pela média dos valores presentes.
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
print(imputer)

# Ajusta o imputer aos dados, calculando a média das colunas (exceto a primeira) e substituindo os valores ausentes.
imputer = imputer.fit(x[:,1:3])
print(imputer)