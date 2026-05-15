import streamlit as st
import pandas as pd
import plotly.express as px # <-- Trouxemos a biblioteca de gráficos

# 1. Configuração inicial da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Dashboard Analítico de Vendas")
st.write("Acompanhamento de faturamento e desempenho dos produtos.")

# 2. Carregando e tratando os dados
@st.cache_data
def carregar_dados():
    # CUIDADO: Mantenha o caminho completo que você copiou aí no seu computador
    df = pd.read_csv(r'../dados/stores_sales_forecasting.csv', encoding='latin1')
    
    # Padronizando os nomes das colunas
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)
    
    # TRADUZINDO OS DADOS DIRETO NO PYTHON (Substituindo o inglês original)
    df['subcategory'] = df['subcategory'].replace({
        'Furnishings': 'Decoração',
        'Tables': 'Mesas',
        'Bookcases': 'Estantes',
        'Chairs': 'Cadeiras'
    })
    
    df['region'] = df['region'].replace({
        'South': 'Sul',
        'West': 'Oeste',
        'East': 'Leste',
        'Central': 'Central'
    })
    
    # Convertendo as datas
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Criando a coluna de Mês/Ano
    df['mes_ano'] = df['order_date'].dt.to_period('M').astype(str)
    
    return df

df = carregar_dados()

# 3. Cards de Indicadores Principais
st.subheader("Métricas Gerais")
col1, col2 = st.columns(2)

col1.metric("Faturamento Total", f"US$ {df['sales'].sum():,.2f}")
col2.metric("Quantidade Total Vendida", df['quantity'].sum())

st.divider()

# 4. Gráficos
col3, col4 = st.columns(2)

with col3:
    # CORREÇÃO 1: Usando subcategory para ver Mesas, Cadeiras, etc.
    st.subheader("Vendas por Sub-Categoria")
    vendas_subcategoria = df.groupby('subcategory')['sales'].sum()
    st.bar_chart(vendas_subcategoria)

with col4:
    st.subheader("Proporção de Vendas por Região")
    vendas_regiao = df.groupby('region')['sales'].sum().reset_index()
    
    # Montando a rosca com Plotly
    grafico_rosca = px.pie(vendas_regiao, values='sales', names='region', hole=0.5)
    
    # Formatando o balão de informações de forma blindada
    grafico_rosca.update_traces(
        textinfo='percent',
        hovertemplate='<b>Região:</b> %{label}<br><b>Faturamento:</b> US$ %{value:,.2f}<extra></extra>'
    )
    
    # Desativando o tema padrão do Streamlit para o balão ficar com a cor da fatia
    st.plotly_chart(grafico_rosca, use_container_width=True, theme=None)

st.subheader("Evolução Mensal das Vendas")
vendas_mes = df.groupby('mes_ano')['sales'].sum()
st.line_chart(vendas_mes)
