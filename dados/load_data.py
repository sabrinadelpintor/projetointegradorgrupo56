import pandas as pd
import sqlite3

# 1 - carregar os dados 
df = pd.read_csv('stores_sales_forecasting.csv', encoding='latin1')

# 2 - Conectando ao banco de dados SQLite (vai criar o arquivo vendas.db na mesma pasta)
conn = sqlite3.connect('vendas.db')

# 3 - Salvando os dados no banco na tabela correta 
df.to_sql('vendas_forecast', conn, if_exists='replace', index=False)

# Mensagem de sucesso corrigida
print("Dados carregados com sucesso!")

# Fechando a conexão corretamente
conn.close()
      
