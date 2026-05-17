import panda as pd
import sqlite3

# 1 -carregar os dados 
df = pd.read_csv('dados/stores_sales_forecasting.csv')

# 2 - Conectar ao banco (cria se não existir)
conn = sqlite3.connect('database/vendas.db')

# 3 - Salvar ps dadps na tabela 
df.to_sql('vendas_forescast', conn, if_exists='replace', index=False)

print("Dados carregados com sucesso!)
      conn. close()
      
