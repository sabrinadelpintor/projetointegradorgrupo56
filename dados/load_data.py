import pandas as pd
import sqlite3

# 1. Carregar os dados
df = pd.read_csv('data/raw/stores_sales_forecasting.csv')

# 2. Conectar ao banco (cria se não existir)
conn = sqlite3.connect('database/vendas.db')

# 3. Salvar os dados na tabela
df.to_sql('vendas_forecast', conn, if_exists='replace', index=False)

print("Dados carregados com sucesso!")
conn.close()
