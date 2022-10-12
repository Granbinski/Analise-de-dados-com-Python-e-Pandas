import pandas as pd     # importa a biblioteca pandas

df = pd.read_csv('..arquivo.csv', error_bad_lines=False, sep=';')
print(df)

# Vizualizando as 5 primeiras linhas
print(df.head())

df.rename(columns={"country": "Pais", "continent": "continente"})

df.head(10)  # exibe as 10 primeiras linhas

df.shape  # total de linhas e colunas

df.columns  # Retorna as colunas

df.dtypes  # Como esta sendo armazenado

# O final das linhas do conjunto de daods, podendo ser alterado o valor(?)
df.tail

df.describe()

df["continent"].unique()  # Retorna valores de continent

Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()

Oceania["continente"].unique()
pd.array(['Oceania'], dtypes=object)

df.groupby("continente")["Pais"].nunique()

df.groupby("ano")["Expectativa de vida"].mean()

df["PIB"].mean()

df["PIB"].sun()
