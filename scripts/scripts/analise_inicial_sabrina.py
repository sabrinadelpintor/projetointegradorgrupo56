import pandas as pd

# carregando a base (ajustado pra estrutura com /scripts e /dados)
df = pd.read_csv('../dados/stores_sales_forecasting.csv', encoding='latin1')

print("Colunas do dataset:")
print(df.columns)

# visualização inicial
print("\nPrimeiras linhas:")
print(df.head())

# informações gerais
print("\nInformações do dataset:")
print(df.info())

# valores nulos
print("\nValores nulos:")
print(df.isnull().sum())

# convertendo data
df['Order Date'] = pd.to_datetime(df['Order Date'])

# criando coluna de mês/ano
df['AnoMes'] = df['Order Date'].dt.to_period('M')

# métricas principais
print("\nFaturamento total:")
print(df['Sales'].sum())

print("\nQuantidade total vendida:")
print(df['Quantity'].sum())

# análise por categoria
print("\nVendas por categoria:")
print(df.groupby('Category')['Sales'].sum())

# análise por região
print("\nVendas por região:")
print(df.groupby('Region')['Sales'].sum())

# evolução no tempo
print("\nVendas por mês:")
print(df.groupby('AnoMes')['Sales'].sum().head())

# Dados prontos para uso futuro no dashboard (Streamlit)
